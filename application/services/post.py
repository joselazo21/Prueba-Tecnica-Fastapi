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
            tags = await tags_service.filter_tags(
                filters=(
                TagSchemaFilter(ids_in=new_post.tags)
                )
            )
    
        return await self.repo.create_post(
            title=new_post.title,
            content=new_post.content,
            owner_id=owner_id,
            tags=tags
        )
    

class PostFilterService:
    def __init__(self, db: AsyncSession):
        self.repo = PostRepository(db)

    async def filter(self, filters):
        return await self.repo.filter_posts(filters)