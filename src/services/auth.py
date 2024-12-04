from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from pathlib.context import CryptContext
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
    def get_password(self, password:str):
        return self.pwd_context.hash(password)
