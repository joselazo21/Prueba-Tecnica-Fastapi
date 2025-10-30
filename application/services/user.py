from infrastructure.respositories.user import UserRepository
from domain.models.user import User
from database import get_db as db
from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from utils.auth import get_password_hash


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
    
    async def get_by_email(self, email: str):
        return await self.repo.get_user_by_email(email)
    
    async def get_all_users(self):
        return await self.repo.get_all_users()
    
    async def filter_users(self, filters, page: int, page_size: int):
        return await self.repo.filter_users(filters, page, page_size)
    

class UserDeleteService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    async def delete_user(self, user: User):
        await self.repo.delete_user(user)


class UserUpdateService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    async def update_user(self, new_data, user: User):
        return await self.repo.update_user(new_data, user)