from sqlalchemy.orm import Session
from infrastructure.orm.tables import Tag
from domain.models.tag import TagCreateModel
from domain.filters.tag import TagSchemaFilter
from infrastructure.filters.tag import TagFilterSet

class TagRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_tag(self, tag: TagCreateModel) -> Tag:
        db_tag = Tag(name=tag.name)
        self.db.add(db_tag)
        self.db.commit()
        self.db.refresh(db_tag)
        return db_tag
    
    def filter_tags(self, filters: TagSchemaFilter):
        query = self.db.query(Tag)
        filter_set = TagFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        return query.all()
    
