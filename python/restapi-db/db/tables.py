import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from openapi_server.db.setting import Base
from openapi_server.db.setting import ENGINE


class Users(Base):
    __tablename__ = 'users'
    id = Column(String(40), primary_key=True)
    name = Column(String(255))
    email = Column(String(255))

    def dump(self):
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}


def init_tables():
    Base.metadata.create_all(bind=ENGINE)
