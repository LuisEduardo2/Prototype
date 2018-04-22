from sqlalchemy.ext.declarative import declarative_base
from app import engine

Base = declarative_base()

#create database schema if not exist
from app.models.contacts import Contacts

Base.metadata.create_all(engine)