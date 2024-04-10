import uuid

from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from fastapi import Depends


from core.models.users import User, get_user

SECRET = "TOTALLY_SECRET"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user)):
    yield UserManager(user_db)
