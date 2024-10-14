from models import UserCreate
from db import database

class UserService:
    user_model = database["users"]

    @staticmethod
    async def user_register(user: UserCreate):
        user_data = user
        # result = await user_model.insert_one(user)
        # return user_create
        return user_data