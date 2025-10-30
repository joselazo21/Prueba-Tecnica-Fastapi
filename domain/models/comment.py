from pydantic import BaseModel, Field

class CommentCreateModel(BaseModel):
    content: str = Field(..., max_length=500)


class CommentResponseModel(BaseModel):
    id: int 
    content: str
    author_id: int
    post_id: int
