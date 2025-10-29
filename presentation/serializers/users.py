
from infrastructure.orm.tables import User
from domain.models.user import UserResponse

class UserMapper:

    def to_api_response(self, user: User) -> UserResponse:
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
        )