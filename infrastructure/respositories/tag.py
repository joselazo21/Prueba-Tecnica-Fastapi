from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.orm.tables import Tag
from domain.models.tag import TagCreateModel
from domain.filters.tag import TagSchemaFilter
from infrastructure.filters.tag import TagFilterSet
from sqlalchemy import select

class TagRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_tag(self, tag: TagCreateModel) -> Tag:
        print(f"Session: {self.db}")
        db_tag = Tag(name=tag.name)
        self.db.add(db_tag)
        await self.db.commit()
        await self.db.refresh(db_tag)
        return db_tag
    
    async def filter_tags(self, filters: TagSchemaFilter):
        query = select(Tag)
        filter_set = TagFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        result = await self.db.execute(query)
        tags = result.scalars().all()
        return tags
    
    async def delete_tag(self, tag: Tag):
        tag.soft_delete()
        await self.db.commit()
    
