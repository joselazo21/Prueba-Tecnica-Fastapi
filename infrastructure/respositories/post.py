from infrastructure.orm.tables import Post
from domain.filters.post import PostSchemaFilter
from infrastructure.filters.post import PostFilterSet
from sqlalchemy import select

class PostRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_post(self, title: str, content: str, owner_id: int):
        new_post = Post(title=title, content=content, owner_id=owner_id)
        self.db_session.add(new_post)
        self.db_session.commit()
        self.db_session.refresh(new_post)
        return new_post
    
    def filter_posts(self, filters: PostSchemaFilter):
        query = select(Post)
        filter_set = PostFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        result = self.db_session.execute(query)
        return result.scalars().all()
       