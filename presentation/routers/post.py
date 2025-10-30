from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from domain.models.user import User
from domain.models.post import PostCreateModel
from utils.auth import get_current_user
from application.services.post import PostCreateService, PostFilterService
from presentation.serializers.post import PostMapper
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from domain.filters.post import PostSchemaFilter
from infrastructure.respositories.post import PostRepository
from infrastructure.orm.tables import Post
from application.services.post import PostDeleteService
from utils.permissions import check_permission

postRouter = APIRouter()

@postRouter.post("")
async def get_posts(
    new_post: PostCreateModel,
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    post_mapper = PostMapper()
    post_service = PostCreateService(db)

    created_post = await post_service.create(new_post, owner_id=user.id)

    return post_mapper.to_api_response(created_post)


@postRouter.get("")
async def filter_posts( 
    db: Annotated[AsyncSession, Depends(get_db)],
    auth_user: Annotated[User, Depends(get_current_user)],
    filters: Annotated[PostSchemaFilter, Depends()] = None,
):
    post_mapper = PostMapper()
    post_service = PostFilterService(db)

    filtered_posts = await post_service.filter(filters)

    responses = []

    for post in filtered_posts:
        responses.append(post_mapper.to_api_response(post))

    return responses


@postRouter.delete("/{post_id}")
async def delete_post(
    post_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
    auth_user: Annotated[User, Depends(get_current_user)],
):
    post_list_service = PostFilterService(db)
    post_delete_service = PostDeleteService(db)

    posts = await post_list_service.filter(PostSchemaFilter(id=post_id))

    if not posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    post = posts[0]

    check_permission(auth_user.id, post.owner_id)

    await post_delete_service.delete(post)

    return {"detail": "Post deleted successfully"}

    