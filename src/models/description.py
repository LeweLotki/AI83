from sqlalchemy import Column, String, Integer
from . import Base

class TableDescription(Base):
    __tablename__ = 'description'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    content = Column(String, nullable=False)

    def __repr__(self):
        return f'<name: {self.name}, content: {self.content}>'
