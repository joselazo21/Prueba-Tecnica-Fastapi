from infrastructure.orm.tables import Post, Tag
from domain.filters.post import PostSchemaFilter
from infrastructure.filters.post import PostFilterSet
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from application.services.tag import TagFilterService

class PostRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    async def create_post(self, title: str, content: str, owner_id: int, tags:list[Tag] | None = None):
        new_post = Post(title=title, content=content, owner_id=owner_id, tags=tags)
        await self.db_session.add(new_post)
        await self.db_session.commit()
        await self.db_session.refresh(new_post)
        return new_post
    
    async def filter_posts(self, filters: PostSchemaFilter):
        query = select(Post).options(
            selectinload(Post.tags),
            selectinload(Post.comments)
        )
        filter_set = PostFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        result = await self.db_session.execute(query)
        return result.scalars().all()
       