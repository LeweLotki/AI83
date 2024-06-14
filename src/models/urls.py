from sqlalchemy import Column, String, Integer, Boolean
from . import Base


class TableURL(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    scraped = Column(Boolean, default=False)

