from sqlalchemy import orm

from utils.db_api import engine


__all__ = ('Session',)

Session = orm.sessionmaker(bind=engine.engine)
