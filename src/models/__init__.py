import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


Base = declarative_base()

DATABASE_URL = 'sqlite:///instance/database.db'

if not os.path.exists('instance'):
    os.makedirs('instance')

engine = create_engine(DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def init_db():
    from .songs import TableSongs
    from .urls import TableURL
    from .description import TableDescription
    Base.metadata.create_all(engine)

