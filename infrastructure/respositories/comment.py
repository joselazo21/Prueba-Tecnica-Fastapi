from sqlalchemy.orm import Session
from sqlalchemy import select
from infrastructure.filters.comment import CommentFilterSet
from infrastructure.orm.tables import Comments
from domain.models.comment import CommentCreateModel
from domain.filters.comment import CommentSchemaFilter

class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, comment: CommentCreateModel, author_id: int, post_id: int) -> Comments:
        db_comment = Comments(content=comment.content, author_id=author_id, post_id=post_id)
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment
    

    def filter_comments(self, filters: CommentSchemaFilter):
        query = select(Comments)
        filter_set = CommentFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        result = self.db.execute(query).scalars().all()
        return result