from infrastructure.respositories.post import PostRepository
from domain.models.post import PostCreateModel
from sqlalchemy.orm import Session
from application.services.tag import TagFilterService
from domain.filters.tag import TagSchemaFilter

class PostCreateService:
    def __init__(self, db: Session):
        self.repo = PostRepository(db)

    def create(self, new_post:PostCreateModel, owner_id:int):
        tags_service = TagFilterService(self.repo.db_session)
        if new_post.tags:
            tags = tags_service.filter_tags(
                filters=(
                TagSchemaFilter(ids_in=new_post.tags)
                )
            )

        return self.repo.create_post(
            title=new_post.title,
            content=new_post.content,
            owner_id=owner_id,
            tags=tags
        )
    

class PostFilterService:
    def __init__(self, db: Session):
        self.repo = PostRepository(db)

    def filter(self, filters):
        return self.repo.filter_posts(filters)