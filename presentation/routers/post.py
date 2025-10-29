from fastapi import APIRouter, Depends
from typing import Annotated
from domain.models.user import User
from domain.models.post import PostCreateModel
from utils.auth import get_current_user
from application.services.post import PostCreateService
from presentation.serializers.post import PostMapper
from sqlalchemy.orm import Session
from database import get_db

postRouter = APIRouter()

@postRouter.post("")
async def get_posts(
    new_post: PostCreateModel,
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    post_mapper = PostMapper()
    post_service = PostCreateService(db)

    created_post = post_service.create(new_post, owner_id=user.id)

    return post_mapper.to_api_response(created_post)
    