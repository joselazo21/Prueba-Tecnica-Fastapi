from fastapi import APIRouter, Depends
from typing import Annotated
from domain.models.user import User
from utils.auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from application.services.user import UserListService
from presentation.serializers.users import UserMapper


userRouter = APIRouter()

@userRouter.get("")
async def get_users(
    db: Annotated[Session, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],  
):
    user_service = UserListService(db)
    user_mapper = UserMapper()
    users = user_service.get_all_users()
    
    responses = []

    for user in users:
        responses.append(user_mapper.to_api_response(user))

    return responses


