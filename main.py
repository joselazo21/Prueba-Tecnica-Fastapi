from fastapi import FastAPI
from database import engine 
from database import Base
from infrastructure.orm.tables import User 
from presentation.routers import auth, user, post, comment, tag
from presentation.middleware import CustomMiddleware

from database import create_tables

create_tables()

app = FastAPI(title="Mi API con SQLAlchemy", version="1.0")
app.include_router(auth.authRouter, prefix="/auth", tags=["auth"])
app.include_router(user.userRouter, prefix="/users", tags=["users"])
app.include_router(post.postRouter, prefix="/posts", tags=["posts"])
app.include_router(comment.commentRouter, prefix="/comments", tags=["comments"])
app.include_router(tag.tagRouter, prefix="/tags", tags=["tags"])

app.add_middleware(CustomMiddleware)



@app.get("/")
def read_root():
    return {"mensaje": "¡API funcionando con PostgreSQL y SQLAlchemy!"}