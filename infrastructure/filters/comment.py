from sqlalchemy_filterset import BaseFilterSet, Filter
from infrastructure.orm.tables import Comments

class CommentFilterSet(BaseFilterSet):
    id = Filter(Comments.id)
    content = Filter(Comments.content)
    author_id = Filter(Comments.author_id)
    post_id = Filter(Comments.post_id)

