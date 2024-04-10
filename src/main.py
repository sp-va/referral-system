import uvicorn

from fastapi import FastAPI

from api.auth_backend import fastapi_users, auth_backend
from api.schemas.users import UserRead, UserCreate

app = FastAPI(
    title="Referral system",
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)