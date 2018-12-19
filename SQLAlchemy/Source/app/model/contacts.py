from sqlalchemy import Column, String, Integer
from app.model import Base

class Contacts(Base):
    __tablename__ = 'contatos'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fone = Column(String)

    def __init__(self, name, fone):
        self.name = name
        self.fone = fone