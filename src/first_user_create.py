import asyncio

from utils.create_user import create_user

if __name__ == "__main__":
    asyncio.run(create_user(
        username="Username",
        email="mail@mail.com",
        password="qwe",
    ))
