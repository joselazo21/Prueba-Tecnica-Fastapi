from pydantic import BaseModel

class UserSchemaFilter(BaseModel):
    id: int | None = None
    username: str | None = None
    email: str | None = None
    full_name: str | None = None