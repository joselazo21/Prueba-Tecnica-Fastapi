from pydantic import BaseModel  
from typing import List
from fastapi import Query

class TagSchemaFilter(BaseModel):
    id: int | None = None
    name: str | None = None