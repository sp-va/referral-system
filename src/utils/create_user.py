import contextlib

import uuid

from db.base import get_async_session
from core.user_manager import get_user_manager
from core.models.users import get_user
from api.schemas.users import UserCreate
from fastapi_users.exceptions import UserAlreadyExists

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(username: str, email: str, password: str, is_superuser: bool = False):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            username=username,
                            email=email,
                            password=password,
                            is_superuser=is_superuser,
                        )
                    )
                    print(f"User created {user}")
                    return user
    except UserAlreadyExists:
        print(f"User {email} already exists")
        raise UserAlreadyExists