import datetime

import sqlalchemy

from utils.db_api import base


class BaseModel(base.Base):
    __abstract__ = True

    id = sqlalchemy.Column(
        sqlalchemy.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    created_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    updated_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return f"{type(self).__name__}(id={self.id})"
