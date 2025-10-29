from sqlalchemy import Column, Boolean
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)