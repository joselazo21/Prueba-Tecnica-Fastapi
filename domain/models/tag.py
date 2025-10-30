from pydantic import BaseModel

class TagCreateModel(BaseModel):
    name: str


class TagUpdateModel(BaseModel):
    name: str | None = None


class TagResponseModel(BaseModel):
    id: int
    name: str