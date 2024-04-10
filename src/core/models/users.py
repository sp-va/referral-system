import uuid

from fastapi import Depends

from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UniqueConstraint

from core.models.base_model import Base
from db.base import get_async_session


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    referral_code: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4())
    parent_referral_code: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.referral_code"), nullable=False)

    children: Mapped["User"] = relationship("User", back_populates="parent")
    parent: Mapped["User"] = relationship("User", back_populates="children", remote_side=[id])


async def get_user(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
