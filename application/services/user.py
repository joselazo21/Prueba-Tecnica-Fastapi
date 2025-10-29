from infrastructure.respositories.user import UserRepository
from domain.models.user import User
from database import get_db as db

class UserCreateService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    async def create(self, user:User):
        return await self.repo.create_user(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            hashed_password=user.password
        )
    

class UserListService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    async def get_by_id(self, user_id: int):
        return await self.repo.get_user_by_id(user_id)

    async def get_by_username(self, username: str):
        return await self.repo.get_user_by_username(username) 
    
    async def get_all_users(self):
        return await self.repo.get_all_users()
    
    async def filter_users(self, filters):
        return await self.repo.filter_users(filters)
    

class UserDeleteService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    async def delete_user(self, user: User):
        await self.repo.delete_user(user)