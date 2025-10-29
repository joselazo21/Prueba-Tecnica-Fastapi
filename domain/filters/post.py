from pydantic import BaseModel

class PostSchemaFilter(BaseModel):
    id: int | None = None
    title: str | None = None
    content: str | None = None
    owner_id: int | None = None