from domain.models.comment import CommentResponseModel
from infrastructure.orm.tables import Comments

class CommentMapper:

    def to_api_response(self, comment: Comments):
        return CommentResponseModel(
            id=comment.id,
            content=comment.content,
            author_id=comment.author_id,
            post_id=comment.post_id,
        )