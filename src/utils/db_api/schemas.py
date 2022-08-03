from sqlalchemy import sql
import sqlalchemy

from utils.db_api import base


class BaseModel(base.Base):
    __abstract__ = True

    id = sqlalchemy.Column(
        sqlalchemy.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    created_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP, server_default=sql.func.now())
    updated_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP, onupdate=sql.func.current_timestamp())

    def __repr__(self):
        return f"{type(self).__name__}(id={self.id})"
