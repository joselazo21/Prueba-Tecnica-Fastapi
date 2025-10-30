from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from application.services.user import UserCreateService, UserListService
from presentation.serializers.users import UserMapper
from config import Config
from database import get_db
from domain.models.auth import Token
from domain.models.user import User
from utils.auth import authenticate_user, create_access_token, get_password_hash

authRouter = APIRouter()

@authRouter.post("/register")
async def register_user(user: User, db: AsyncSession  = Depends(get_db)):
    user_create_service = UserCreateService(db)
    user_list_service = UserListService(db)
    user_mapper = UserMapper()

    existing_user = await user_list_service.get_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered.")
    
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    new_user = await user_create_service.create(user)
    
    return user_mapper.to_api_response(new_user)
    

@authRouter.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db),
) -> Token:
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")