from sqlalchemy.orm import Session
from infrastructure.orm.tables import Comments
from domain.models.comment import CommentCreateModel

class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, comment: CommentCreateModel, author_id: int, post_id: int) -> Comments:
        db_comment = Comments(content=comment.content, author_id=author_id, post_id=post_id)
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment