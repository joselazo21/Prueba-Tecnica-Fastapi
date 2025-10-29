from pydantic import BaseModel

class CommentSchemaFilter(BaseModel):
    id: int | None = None
    content: str | None = None
    author_id: int | None = None
    post_id: int | None = None