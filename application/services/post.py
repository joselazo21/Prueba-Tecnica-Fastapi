from infrastructure.respositories.post import PostRepository
from domain.models.post import PostCreateModel
from sqlalchemy.ext.asyncio import AsyncSession
from application.services.tag import TagFilterService
from domain.filters.tag import TagSchemaFilter

class PostCreateService:
    def __init__(self, db: AsyncSession):
        self.repo = PostRepository(db)

    async def create(self, new_post:PostCreateModel, owner_id:int):
        tags_service = TagFilterService(self.repo.db_session)

        if new_post.tags:
            tags = await tags_service.get_tags_by_ids(new_post.tags)
    
        return await self.repo.create_post(
            title=new_post.title,
            content=new_post.content,
            owner_id=owner_id,
            tags=tags if new_post.tags else None,
        )
    

class PostFilterService:
    def __init__(self, db: AsyncSession):
        self.repo = PostRepository(db)

    async def filter(self, filters, page:int=1, page_size:int=10):
        return await self.repo.filter_posts(filters)
    

class PostDeleteService:
    def __init__(self, db: AsyncSession):
        self.repo = PostRepository(db)

    async def delete(self, post):
        await self.repo.delete_post(post)


class PostUpdateService:
    def __init__(self, db: AsyncSession):
        self.repo = PostRepository(db)

    async def update(self, new_data, post):
        return await self.repo.edit_post(new_data, post)