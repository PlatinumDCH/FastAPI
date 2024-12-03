from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from pathlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt
from starlette import status
