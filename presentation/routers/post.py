from fastapi import APIRouter, Depends
from typing import Annotated
from domain.models.user import User
from domain.models.post import PostCreateModel
from utils.auth import get_current_user
from application.services.post import PostCreateService, PostFilterService
from presentation.serializers.post import PostMapper
from sqlalchemy.orm import Session
from database import get_db
from domain.filters.post import PostSchemaFilter

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


@postRouter.get("")
async def filter_posts( 
    db: Annotated[Session, Depends(get_db)],
    auth_user: Annotated[User, Depends(get_current_user)],
    filters: Annotated[PostSchemaFilter, Depends()] = None,
):
    post_mapper = PostMapper()
    post_service = PostFilterService(db)

    filtered_posts = post_service.filter(filters)

    responses = []

    for post in filtered_posts:
        responses.append(post_mapper.to_api_response(post))

    return responses

    