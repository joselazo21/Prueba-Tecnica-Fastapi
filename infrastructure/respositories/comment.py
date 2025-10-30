from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from infrastructure.filters.comment import CommentFilterSet
from infrastructure.orm.tables import Comments
from domain.models.comment import CommentCreateModel, CommentUpdateModel
from domain.filters.comment import CommentSchemaFilter

class CommentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_comment(self, comment: CommentCreateModel, author_id: int, post_id: int) -> Comments:
        db_comment = Comments(content=comment.content, author_id=author_id, post_id=post_id)
        self.db.add(db_comment)
        await self.db.commit()
        await self.db.refresh(db_comment)
        return db_comment
    

    async def filter_comments(self, filters: CommentSchemaFilter, page:int=1, page_size:int=10):
        query = select(Comments)
        query = Comments.active(query)
        filter_set = CommentFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        query = query.offset((page - 1) * page_size).limit(page_size)
        result = await self.db.execute(query)
        comments = result.scalars().all()
        return comments
    
    async def delete_comment(self, comment: Comments):
        comment.soft_delete()
        await self.db.commit()

    async def update_comment(self, new_data: CommentUpdateModel, comment: Comments):
        for field, value in new_data.model_dump(exclude_unset=True).items():
            setattr(comment, field, value)
        self.db.add(comment)
        await self.db.commit()
        await self.db.refresh(comment)
        return comment
    