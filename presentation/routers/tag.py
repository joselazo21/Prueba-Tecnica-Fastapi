from fastapi import APIRouter, Depends
from domain.models.tag import TagCreateModel
from typing import Annotated
from domain.models.user import User
from sqlalchemy.orm import Session
from utils.auth import get_current_user
from application.services.tag import TagCreateservice
from presentation.serializers.tag import TagMapper
from database import get_db

tagRouter = APIRouter()

@tagRouter.post("")
async def create_tag(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    tag: TagCreateModel,
):
    tag_mapper = TagMapper()
    tag_service = TagCreateservice(db)

    created_tag = tag_service.create_tag(tag)

    return tag_mapper.to_api_response(created_tag)