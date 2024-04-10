import uuid

from fastapi_users import schemas


class BaseUser:
    username: str


class UserRead(schemas.BaseUser[uuid.UUID], BaseUser):
    referral_code: uuid.UUID
    parent_referral_code: uuid.UUID


class UserCreate(schemas.BaseUserCreate, BaseUser):
    referral_code: uuid.UUID


class UserUpdate(schemas.BaseUserUpdate, BaseUser):
    pass
