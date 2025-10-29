from infrastructure.orm.tables import Post

class PostRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_post(self, title: str, content: str, owner_id: int):
        new_post = Post(title=title, content=content, owner_id=owner_id)
        self.db_session.add(new_post)
        self.db_session.commit()
        self.db_session.refresh(new_post)
        return new_post