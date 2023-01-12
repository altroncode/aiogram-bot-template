from sqlalchemy import orm

from database import engine


__all__ = ('Session',)


Session = orm.sessionmaker(bind=engine.engine)
