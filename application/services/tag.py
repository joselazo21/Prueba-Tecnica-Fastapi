from sqlalchemy.orm import Session
from infrastructure.respositories.tag import TagRepository
from domain.models.tag import TagCreateModel

class TagCreateservice:
    def __init__(self, db: Session):
        self.tag_repository = TagRepository(db)

    def create_tag(self, tag: TagCreateModel):
        return self.tag_repository.create_tag(tag)