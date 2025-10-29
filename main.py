from fastapi import FastAPI
from database import engine 
from database import Base
from infrastructure.orm.tables import User 
from presentation.routers import auth, user, post

from database import create_tables

create_tables()

app = FastAPI(title="Mi API con SQLAlchemy", version="1.0")
app.include_router(auth.authRouter, prefix="/auth", tags=["auth"])
app.include_router(user.userRouter, prefix="/users", tags=["users"])
app.include_router(post.postRouter, prefix="/posts", tags=["posts"])


@app.get("/")
def read_root():
    return {"mensaje": "¡API funcionando con PostgreSQL y SQLAlchemy!"}