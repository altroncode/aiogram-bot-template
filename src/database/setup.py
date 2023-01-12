from database import base, engine


def setup_database():
    base.Base.metadata.create_all(engine.engine)
