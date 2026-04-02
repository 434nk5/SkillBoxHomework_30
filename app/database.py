from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "recipes.db"
DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_FILE}"


class Base(DeclarativeBase):
    pass


engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    async with SessionLocal() as session:
        yield session