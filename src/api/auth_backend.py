import uuid

import redis.asyncio

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, RedisStrategy, AuthenticationBackend

from core.models.users import User
from core.user_manager import get_user_manager

cookie_transport = CookieTransport(cookie_max_age=3600)

redis = redis.asyncio.from_url("redis://localhost:6379", decode_responses=True)


def get_redis_strategy():
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_redis_strategy
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
