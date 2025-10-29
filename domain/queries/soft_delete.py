from sqlalchemy.orm import Query
from domain.mixins.soft_delete import SoftDeleteMixin

class SoftDeleteQuery(Query):
    def __new__(cls, entities, session=None):
        query = super().__new__(cls, entities, session)
        return query

    def __init__(self, entities, session=None):
        super().__init__(entities, session)
        self._apply_soft_delete_filter()

    def _apply_soft_delete_filter(self):
        """Aplica filtro is_deleted=False a cualquier entidad que herede de SoftDeleteMixin"""
        if self._entities:
            for entity in self._entities:
                mapper = entity.mapper
                if issubclass(mapper.class_, SoftDeleteMixin):
                    self = self.filter(mapper.class_.is_deleted.is_(False))
        return self