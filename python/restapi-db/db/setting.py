from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

ENGINE = create_engine('sqlite:///sample_db.sqlite3', echo=True)

session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
))

Base = declarative_base()
Base.query = session.query_property()
