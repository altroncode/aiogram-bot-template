from sqlalchemy import orm

from utils.db_api import engine


Session = orm.sessionmaker(bind=engine.engine)
