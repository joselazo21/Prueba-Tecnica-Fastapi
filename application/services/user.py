from infrastructure.respositories.user import UserRepository
from domain.models.user import User
from database import get_db as db

class UserCreateService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def create(self, user:User):
        return self.repo.create_user(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            hashed_password=user.password
        )
    

class UserListService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def get_by_id(self, user_id: int):
        return self.repo.get_user_by_id(user_id)

    def get_by_username(self, username: str):
        return self.repo.get_user_by_username(username) 
    
    def get_all_users(self):
        return self.repo.get_all_users()
    
    def filter_users(self, filters):
        return self.repo.filter_users(filters)
    

class UserDeleteService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def delete_user(self, user: User):
        self.repo.delete_user(user)