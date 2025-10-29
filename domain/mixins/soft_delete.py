from sqlalchemy import Column, Boolean, select
from sqlalchemy.orm import declarative_mixin, Query
from datetime import datetime


@declarative_mixin
class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)

    def soft_delete(self) -> None:
        self.is_deleted = True
        self.deleted_at = datetime.utcnow()

    def restore(self) -> None:
        self.is_deleted = False
        self.deleted_at = None

    @classmethod
    def deleted(cls) -> Query:
        return select(cls).where(cls.is_deleted.is_(True))