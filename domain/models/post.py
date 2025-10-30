from pydantic import BaseModel, Field

class PostCreateModel(BaseModel):
    title: str = Field(..., max_length=200)
    content: str = Field(..., max_length=2000)
    tags: list[int] | None = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    tags: list[str]
    comments: list[str]