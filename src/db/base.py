from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.db.config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    expire_on_commit=False
)


async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session
