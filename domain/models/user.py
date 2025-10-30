from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(..., max_length=150)
    email: EmailStr = Field(...)
    full_name: str = Field(..., max_length=100)
    password: str = Field(..., min_length=20)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str


class UserUpdateModel(BaseModel):
    email: EmailStr | None = Field(None)
    username: str | None = Field(None, max_length=150)