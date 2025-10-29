from pydantic import BaseModel  

class TagSchemaFilter(BaseModel):
    id: int | None = None
    name: str | None = None
    ids_in: list[int] | None = None