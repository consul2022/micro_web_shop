from pydantic import BaseModel
import datetime


class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str


class User(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    phone: int

class Book(BaseModel):
    id: int
    name: str
    author: str
    description: str
    date_published: datetime
    price: float


