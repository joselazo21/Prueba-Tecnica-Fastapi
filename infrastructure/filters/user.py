from sqlalchemy_filterset import BaseFilterSet, Filter
from infrastructure.orm.tables import User 


class UserFilterSet(BaseFilterSet):
    id = Filter(User.id)
    username = Filter(User.username)
    email = Filter(User.email)
    full_name = Filter(User.full_name)