import sqlalchemy

import settings


engine = sqlalchemy.create_engine(settings.DATABASE_URI)
