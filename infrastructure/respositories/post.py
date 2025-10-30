from infrastructure.orm.tables import Post, Tag
from domain.filters.post import PostSchemaFilter
from infrastructure.filters.post import PostFilterSet
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from domain.models.post import PostUpdateModel

class PostRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    async def create_post(self, title: str, content: str, owner_id: int, tags:list[Tag] | None = None):
        new_post = Post(title=title, content=content, owner_id=owner_id, tags=tags if tags else [])
        self.db_session.add(new_post)
        await self.db_session.commit()
        await self.db_session.refresh(new_post)

        result = await self.db_session.execute(
            select(Post).options(selectinload(Post.tags), selectinload(Post.comments)).where(Post.id == new_post.id)
        )
        return result.scalar_one()
    
    async def filter_posts(self, filters: PostSchemaFilter):
        query = select(Post).options(
            selectinload(Post.tags),
            selectinload(Post.comments)
        )
        query = Post.active(query)
        
        filter_set = PostFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        result = await self.db_session.execute(query)
        return result.scalars().all()
    
    async def delete_post(self, post: Post):
        post.soft_delete()
        self.db_session.add(post)
        await self.db_session.commit()

    async def edit_post(self, updated_post: PostUpdateModel, post: Post):
        for field, value in updated_post.model_dump(exclude_none=True).items():
            setattr(post, field, value)

        self.db_session.add(post)
        await self.db_session.commit()
        await self.db_session.refresh(post)
        return post

       