from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from domain.models.user import User, UserUpdateModel
from utils.auth import get_current_user
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from application.services.user import UserDeleteService, UserListService, UserUpdateService
from presentation.serializers.users import UserMapper
from domain.filters.user import UserSchemaFilter


userRouter = APIRouter()

@userRouter.get("")
async def get_users(
    db: Annotated[AsyncSession, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],  
    filters: Annotated[UserSchemaFilter, Depends()]
):
    user_service = UserListService(db)
    user_mapper = UserMapper()
    users = await user_service.filter_users(filters=filters)
    
    responses = []

    for user in users:
        responses.append(user_mapper.to_api_response(user))

    return responses

@userRouter.delete("/me")
async def delete_current_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],  
):
    user_service = UserListService(db)
    user_delete_service = UserDeleteService(db)
    user = user_service.get_by_id(authenticated.id)
    if user:
        await user_delete_service.delete_user(user)
        
    return {"detail": "User deleted successfully."}

@userRouter.patch("/me")
async def update_current_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],  
    user_update: UserUpdateModel
):
    user_service = UserListService(db)
    user_update_service = UserUpdateService(db)
    user = await user_service.get_by_id(authenticated.id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    updated_user = await user_update_service.update_user(user_update, user)
    user_mapper = UserMapper()
    return user_mapper.to_api_response(updated_user)

