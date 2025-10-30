from ..orm.tables import User
from sqlalchemy import select
from domain.filters.user import UserSchemaFilter
from domain.models.user import UserUpdateModel
from infrastructure.filters.user import UserFilterSet

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    async def get_user_by_id(self, user_id: int):
        query = select(User).where(User.id == user_id)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def get_user_by_username(self, username: str):
        query = select(User).where(User.username == username)
        query = User.active(query)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def create_user(self, username: str, email: str = None, full_name: str = None, hashed_password: str = None):
        new_user = User(username=username, email=email, full_name=full_name, hashed_password=hashed_password)
        self.db_session.add(new_user)
        await self.db_session.commit()
        await self.db_session.refresh(new_user)
        return new_user
    
    async def get_all_users(self):
        query = select(User).where(User.is_deleted.is_(False))
        result = await self.db_session.execute(query).scalars().all()
        return result
    
    async def filter_users(self, filters: UserSchemaFilter):
        query = select(User)
        filter_set = UserFilterSet(query)
        query = filter_set.filter_query(filters.model_dump(exclude_none=True))
        result = await self.db_session.execute(query).scalars().all()
        return result
    
    async def delete_user(self, user: User):
        user.is_deleted = True
        await self.db_session.commit()

    async def update_user(self, new_data: UserUpdateModel, user: User):
        for field, value in new_data.model_dump(exclude_unset=True).items():
            setattr(user, field, value)
        self.db_session.add(user)
        await self.db_session.commit()
        await self.db_session.refresh(user)
        return user
        