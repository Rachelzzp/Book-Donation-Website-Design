from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True,autoincrement=True)  # primary key & 自增长
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='Unknown')
    isbn = Column(String(15), nullable=False,unique=True)
    price = Column(String(20))
    binding = Column(String(20))
    publisher = Column(String(50))
    pages = Column(Integer)
    pubdate = Column(String(20))
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
