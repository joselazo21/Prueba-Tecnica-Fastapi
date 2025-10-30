from sqlalchemy_filterset import BaseFilterSet, Filter, InFilter
from infrastructure.orm.tables import Tag


class TagFilterSet(BaseFilterSet):
    id = Filter(Tag.id)
    name = Filter(Tag.name)