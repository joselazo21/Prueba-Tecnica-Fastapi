from domain.models.post import PostResponse
from infrastructure.orm.tables import Post

class PostMapper:

    def to_api_response(self, post: Post) -> PostResponse:
        return PostResponse(
            id=post.id,
            title=post.title,
            content=post.content,
            owner_id=post.owner_id,
            tags=[tag.name for tag in post.tags] if post.tags else [],
        )