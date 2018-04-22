from sqlalchemy import Column, String, Integer
from app.models import Base

class Contacts(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fone = Column(String)

    def __init__(self, name, fone):
        self.name = name
        self.fone = fone