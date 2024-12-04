from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt
from starlette import status

from src.database.db import get_db
from src.repository import users as repository_users

class Auth:

    pwd_context = CryptContext(schemes='bcrypt', deprecated='auto')
    SECRET_KEY = '7a4a0a0dd381e393a78d75bfc58a9cbc3bb2c985df98658e3aadf0aef4c4e5bb'
    ALGORITHM = 'HS256'
    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    def get_password_hash(self, password:str):
        return self.pwd_context.hash(password)

    auth2_scheme = OAuth2PasswordBearer(tokenUrl='api/auth/login')


    async def create_access_token(self, data:dict, expires_delta: Optional[float]=None):
        """
        формирует короткий срок для пароля
        :param data
                        {sub": "1234567890",
                        "name": "John Doe",
                        "iat": 1516239022}
        :param expires_delta - можно вручную задать время жизни токена в секундах
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update(
            {'iat':datetime.utcnow(), #кода мы создали токен
             'exp':expire,            #сколько он будет жить
             'scope':'access_token'}  #это значит что это именно access_token
                         )
        encoded_assess_token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_assess_token

    async def create_refresh_token(self, data:dict, expires_delta:Optional[float]=None):
        """Формирует долгий срок для пароля"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(days=7)
        to_encode.update(
            {'iat':datetime.utcnow(), #кода мы создали токен
             'exp':expire,            #сколько он будет жить
             'scope':'refresh_token'}  #это значит что это именно refresh_token
                         )
        encoded_refresh_token = jwt.encode(to_encode, self.SECRET_KEY, self.ALGORITHM)
        return encoded_refresh_token

    async def decode_refresh_token(self, refresh_token:str):
        """Алгоритм в словаре так как это универсальная функция """
        try:
            payload = jwt.decode(refresh_token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            # после того как мы выполнили строчку 67, из токена получим вот такой словарь
            """
            {
            'sub':'1234567890',
            'name':'FirstName SecondName',
            'iat':'13436457687'
            }
            """
            if payload['scope'] == 'refresh_token':
                email = payload['sub']
                return email
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid scope for token')
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')


    async def get_current_user(self, token:str=Depends(auth2_scheme),db:AsyncSession=Depends(get_db)):
        """Вытащить из базы данных пользователя из бд чей токен пришел
        приходит токен jwt on server
        эта функция разбирает этот токен и возвращаем пользователя с бд"""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate':'Bearer'}
        )
        try:
            #Decode JWT
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            if payload['scope'] == 'access_token':
                email=payload['sub'] #subject
                if email is None:
                    raise credentials_exception
            else:
                return credentials_exception
        except JWTError as e:
            raise credentials_exception

        user = await repository_users.get_user_by_email(email, db)
        if user is None:
            raise credentials_exception
        return user

auth_service = Auth()