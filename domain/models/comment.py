from pydantic import BaseModel

class CommentCreateModel(BaseModel):
    content: str


class CommentResponseModel(BaseModel):
    id: int
    content: str
    author_id: int
    post_id: int
