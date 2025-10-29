from pydantic import BaseModel

class PostCreateModel(BaseModel):
    title: str
    content: str
    tags: list[int] | None = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    tags: list[str]
    comments: list[str]