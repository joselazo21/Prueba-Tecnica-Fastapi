from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from database import Base
from domain.mixins.soft_delete import SoftDeleteMixin
from domain.mixins.timestamp import TimestampMixin

post_tag = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class User(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)

    posts = relationship("Post", back_populates="owner")
    comments = relationship("Comments", back_populates="author")


class Post(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship("User", back_populates="posts")

    comments = relationship("Comments", back_populates="post")

    tags = relationship(
        "Tag",
        secondary="post_tag", 
        back_populates="posts"
    )


class Tag(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)

    posts = relationship(
        "Post",
        secondary="post_tag", 
        back_populates="tags"
    )


class Comments(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)

    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship("Post", back_populates="comments")

    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship("User", back_populates="comments")