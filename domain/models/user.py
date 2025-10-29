from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str