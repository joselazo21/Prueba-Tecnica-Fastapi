from fastapi import APIRouter, Depends, HTTPException
from utils.permissions import check_permission
from domain.models.comment import CommentCreateModel, CommentUpdateModel
from typing import Annotated
from domain.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from utils.auth import get_current_user
from application.services.comment import CommentCreateService, CommentDeleteService, CommentListService, CommentUpdateService
from presentation.serializers.comment import CommentMapper
from database import get_db
from domain.filters.comment import CommentSchemaFilter

commentRouter = APIRouter()

@commentRouter.post("/{post_id}")
async def create_comment(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
    comment: CommentCreateModel,
    post_id: int,
):
    comment_mapper = CommentMapper()
    comment_service = CommentCreateService(db)

    created_comment = await comment_service.create_comment(
        comment, author_id=user.id, post_id=post_id
    )

    return comment_mapper.to_api_response(created_comment)


@commentRouter.get("")
async def get_comments(
    db: Annotated[AsyncSession, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],  
    filters: Annotated[CommentSchemaFilter, Depends()]
):
    comment_service = CommentListService(db)
    comment_mapper = CommentMapper()
    comments = await comment_service.filter_comments(filters=filters)
    
    responses = []

    for comment in comments:
        responses.append(comment_mapper.to_api_response(comment))

    return responses

@commentRouter.delete("/{comment_id}")
async def delete_comment(
    comment_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],
):
    comment_service = CommentDeleteService(db)
    comment_list_srv = CommentListService(db)
    
    comment = await comment_list_srv.filter_comments(
        CommentSchemaFilter(id=comment_id)
    )

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    comment = comment[0]
    check_permission(authenticated.id, comment.author_id)
    await comment_service.delete_comment(comment)

    return {"detail": "Comment deleted successfully"}

@commentRouter.patch("/{comment_id}")
async def update_comment(
    comment_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],
    new_data: CommentUpdateModel
):
    comment_list_srv = CommentListService(db)
    comment_update_srv = CommentUpdateService(db)

    comments = await comment_list_srv.filter_comments(
        CommentSchemaFilter(id=comment_id)
    )

    if not comments:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    comment = comments[0]
    check_permission(authenticated.id, comment.author_id)

    updated_comment = await comment_update_srv.update_comment(new_data, comment)
    comment_mapper = CommentMapper()
    return comment_mapper.to_api_response(updated_comment)
