from sqlalchemy_filterset import BaseFilterSet, Filter
from infrastructure.orm.tables import Post
from domain.filters.post import PostSchemaFilter


class PostFilterSet(BaseFilterSet):
    id = Filter(field=Post.id)
    title = Filter(field=Post.title)
    content = Filter(field=Post.content)
    owner_id = Filter(field=Post.owner_id)