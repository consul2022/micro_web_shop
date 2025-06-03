from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DateTime, Foreingkey, Text
from app.db.database import Base
from tomlkit.items import Float


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    phone = Column(Integer, nullable=False)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    date_published = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)



