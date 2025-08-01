import os

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from .models import BaseModel

engine = create_async_engine(os.getenv('DB_LITE'), echo=True)

session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
