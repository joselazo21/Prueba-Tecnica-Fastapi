from fastapi import APIRouter, Depends
from domain.models.comment import CommentCreateModel
from typing import Annotated
from domain.models.user import User
from sqlalchemy.orm import Session
from utils.auth import get_current_user
from application.services.comment import CommentCreateService, CommentListService
from presentation.serializers.comment import CommentMapper
from database import get_db
from domain.filters.comment import CommentSchemaFilter

commentRouter = APIRouter()

@commentRouter.post("/{post_id}")
async def create_comment(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    comment: CommentCreateModel,
    post_id: int,
):
    comment_mapper = CommentMapper()
    comment_service = CommentCreateService(db)

    created_comment = comment_service.create_comment(
        comment, author_id=user.id, post_id=post_id
    )

    return comment_mapper.to_api_response(created_comment)


@commentRouter.get("")
async def get_comments(
    db: Annotated[Session, Depends(get_db)],
    authenticated: Annotated[User, Depends(get_current_user)],  
    filters: Annotated[CommentSchemaFilter, Depends()]
):
    comment_service = CommentListService(db)
    comment_mapper = CommentMapper()
    comments = comment_service.filter_comments(filters=filters)
    
    responses = []

    for comment in comments:
        responses.append(comment_mapper.to_api_response(comment))

    return responses
