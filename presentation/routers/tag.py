from fastapi import APIRouter, Depends, HTTPException
from domain.models.tag import TagCreateModel, TagUpdateModel
from typing import Annotated
from domain.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from utils.auth import get_current_user
from application.services.tag import TagCreateservice, TagFilterService, TagDeleteService, TagEditService
from domain.filters.tag import TagSchemaFilter
from presentation.serializers.tag import TagMapper
from database import get_db


tagRouter = APIRouter()

@tagRouter.post("")
async def create_tag(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
    tag: TagCreateModel,
):
    tag_mapper = TagMapper()
    tag_service = TagCreateservice(db)

    created_tag = await tag_service.create_tag(tag)

    return tag_mapper.to_api_response(created_tag)

@tagRouter.get("")
async def filter_tags(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
    filters: Annotated[TagSchemaFilter, Depends()] = None,
):
    tag_service = TagFilterService(db)
    tags = await tag_service.filter_tags(filters)

    tag_mapper = TagMapper()
    
    return [tag_mapper.to_api_response(tag) for tag in tags]

@tagRouter.delete("/{tag_id}")
async def delete_tag(
    tag_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
    auth_user: Annotated[User, Depends(get_current_user)],
):
    tag_list_service = TagFilterService(db)
    tag_delete_service = TagDeleteService(db)

    tags = await tag_list_service.filter_tags(TagSchemaFilter(id=tag_id))

    if not tags:
        return HTTPException(status_code=404, detail="Tag not found")

    tag = tags[0]

    await tag_delete_service.delete_tag(tag)

    return {"detail": "Tag deleted successfully"}


@tagRouter.patch("/{tag_id}")
async def edit_tag(
    tag_id: int,
    new_data: TagUpdateModel,
    db: Annotated[AsyncSession, Depends(get_db)],
    auth_user: Annotated[User, Depends(get_current_user)],
):
    tag_list_service = TagFilterService(db)
    tag_edit_service = TagEditService(db)

    tags = await tag_list_service.filter_tags(TagSchemaFilter(id=tag_id))

    if not tags:
        return HTTPException(status_code=404, detail="Tag not found")

    tag = tags[0]

    updated_tag = await tag_edit_service.edit_tag(tag, new_data.name)

    tag_mapper = TagMapper()

    return tag_mapper.to_api_response(updated_tag)