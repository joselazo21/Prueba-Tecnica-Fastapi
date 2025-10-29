from ..orm.tables import User

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_user_by_id(self, user_id: int):
        return self.db_session.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str):
        return self.db_session.query(User).filter(User.username == username).first()

    def create_user(self, username: str, email: str = None, full_name: str = None, hashed_password: str = None):
        new_user = User(username=username, email=email, full_name=full_name, hashed_password=hashed_password)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user