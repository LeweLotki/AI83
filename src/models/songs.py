from sqlalchemy import Column, String, Integer
from . import db


class TableSongs(db.Model):

    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    content = Column(String)

    def __repr__(self):
        return f'<name: {self.name}\ncontent: {self.content}>'
