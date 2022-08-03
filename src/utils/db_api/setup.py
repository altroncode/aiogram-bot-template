from utils.db_api import base, engine


def setup_database():
    base.Base.metadata.create_all(engine.engine)
