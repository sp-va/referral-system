import uuid

from fastapi import Depends

from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.base_model import Base
from src.db.base import get_async_session


class User(SQLAlchemyBaseUserTableUUID, Base):
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    referral_code: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4())
    parent_referral_code: Mapped[uuid.UUID] = mapped_column(nullable=False)


async def get_user(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
