from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.respositories.tag import TagRepository
from domain.models.tag import TagCreateModel

class TagCreateservice:
    def __init__(self, db: AsyncSession):
        self.tag_repository = TagRepository(db)

    async def create_tag(self, tag: TagCreateModel):
        return await self.tag_repository.create_tag(tag)
    

class TagFilterService:
    def __init__(self, db: AsyncSession):
        self.tag_repository = TagRepository(db)

    async def filter_tags(self, filters):
        return await self.tag_repository.filter_tags(filters)
    

class TagDeleteService:
    def __init__(self, db: AsyncSession):
        self.tag_repository = TagRepository(db)

    async def delete_tag(self, tag):
        await self.tag_repository.delete_tag(tag)