from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from domain.models.user import User
from domain.models.post import PostCreateModel, PostUpdateModel
from utils.auth import get_current_user
from application.services.post import PostCreateService, PostFilterService, PostUpdateService
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
async def insert_posts(
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
    page: int = 1,
    page_size: int = 10,
):
    post_mapper = PostMapper()
    post_service = PostFilterService(db)

    filtered_posts = await post_service.filter(filters, page, page_size)

    responses = []

    for post in filtered_posts:
        responses.append(post_mapper.to_api_response(post))

    return {
        "posts": responses,
        "total": len(responses),
        "page": page,
        "page_size": page_size,
        "total_pages": (len(responses) + page_size - 1) // page_size
    }


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

@postRouter.patch("/{post_id}")
async def update_post(
    post_id: int,
    updated_data: PostUpdateModel,
    db: Annotated[AsyncSession, Depends(get_db)],
    auth_user: Annotated[User, Depends(get_current_user)],
):
    post_list_service = PostFilterService(db)
    post_update_service = PostUpdateService(db)
    post_mapper = PostMapper()

    posts = await post_list_service.filter(PostSchemaFilter(id=post_id))

    if not posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    post = posts[0]

    check_permission(auth_user.id, post.owner_id)
    updated_post = await post_update_service.update(updated_data, post)

    return post_mapper.to_api_response(updated_post)

    