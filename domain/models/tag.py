from pydantic import BaseModel

class TagCreateModel(BaseModel):
    name: str


class TagResponseModel(BaseModel):
    id: int
    name: str