from fastapi import APIRouter
from models import UserCreate
from services.user_service import UserService

router = APIRouter()

@router.post("/user/register", response_model=UserCreate)
async def user_register(user_create: UserCreate):
    return await UserService.user_register(user_create)