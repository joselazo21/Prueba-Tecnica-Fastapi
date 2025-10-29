from infrastructure.respositories.post import PostRepository
from domain.models.post import PostCreateModel
from sqlalchemy.orm import Session

class PostCreateService:
    def __init__(self, db: Session):
        self.repo = PostRepository(db)

    def create(self, new_post:PostCreateModel, owner_id:int):
        return self.repo.create_post(
            title=new_post.title,
            content=new_post.content,
            owner_id=owner_id
        )
    

class PostFilterService:
    def __init__(self, db: Session):
        self.repo = PostRepository(db)

    def filter(self, filters):
        return self.repo.filter_posts(filters)