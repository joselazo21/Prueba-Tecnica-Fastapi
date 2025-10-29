from sqlalchemy.orm import Session
from infrastructure.respositories.comment import CommentRepository

class CommentCreateService:
    def __init__(self, db: Session):
        self.content = CommentRepository(db)

    def create_comment(self, comment, author_id: int, post_id: int):
        return self.content.create_comment(comment, author_id, post_id)