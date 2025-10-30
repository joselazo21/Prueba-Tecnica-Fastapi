from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.respositories.comment import CommentRepository

class CommentCreateService:
    def __init__(self, db: AsyncSession):
        self.content = CommentRepository(db)

    async def create_comment(self, comment, author_id: int, post_id: int):
        return await self.content.create_comment(comment, author_id, post_id)
    

class CommentListService:
    def __init__(self, db: AsyncSession):
        self.repo = CommentRepository(db)

    async def filter_comments(self, filters):
        return await self.repo.filter_comments(filters)
    

class CommentDeleteService:
    def __init__(self, db: AsyncSession):
        self.repo = CommentRepository(db)

    async def delete_comment(self, comment):
        await self.repo.delete_comment(comment)