from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from infrastructure.filters.comment import CommentFilterSet
from infrastructure.orm.tables import Comments
from domain.models.comment import CommentCreateModel
from domain.filters.comment import CommentSchemaFilter

class CommentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_comment(self, comment: CommentCreateModel, author_id: int, post_id: int) -> Comments:
        print(f"Session: {self.db}")
        db_comment = Comments(content=comment.content, author_id=author_id, post_id=post_id)
        self.db.add(db_comment)
        await self.db.commit()
        await self.db.refresh(db_comment)
        return db_comment
    

    async def filter_comments(self, filters: CommentSchemaFilter):
        query = select(Comments)
        query = Comments.active(query)
        filter_set = CommentFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        result = await self.db.execute(query)
        comments = result.scalars().all()
        return comments
    
    async def delete_comment(self, comment: Comments):
        comment.soft_delete()
        await self.db.commit()