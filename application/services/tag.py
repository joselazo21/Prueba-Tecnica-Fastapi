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

    async def filter_tags(self, filters, page:int=1, page_size:int=10):
        return await self.tag_repository.filter_tags(filters, page, page_size)
    
    async def get_tags_by_ids(self, ids: list[int]):
        return await self.tag_repository.get_tags_by_ids(ids)
    

class TagDeleteService:
    def __init__(self, db: AsyncSession):
        self.tag_repository = TagRepository(db)

    async def delete_tag(self, tag):
        await self.tag_repository.delete_tag(tag)


class TagEditService:
    def __init__(self, db: AsyncSession):
        self.tag_repository = TagRepository(db)

    async def edit_tag(self, tag, new_name: str):
        return await self.tag_repository.edit_tag(tag, new_name)