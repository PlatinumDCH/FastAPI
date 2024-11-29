import contextlib
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.conf.config import config

class Base(DeclarativeBase):
    pass


class DatabaseAsyncSessionManager:
    def __init__(self, url:str):
        self._engine:AsyncEngine | None = create_async_engine(url)
        self._session_maker:async_sessionmaker =  async_sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=self._engine
        )
        @contextlib.asynccontextmanager
        async def session_context(self):
            if self._session_maker is None:
                raise Exception ('Session is not initialized')
            session = self._session_maker()
            try:
                yield session
            except Exception as err:
                await session.rollback()
                raise err
            finally:
                await session.close()

sessionmanager = DatabaseAsyncSessionManager(config.DB_URL)

async def get_db():
    with sessionmanager.session() as session:
        yield session

