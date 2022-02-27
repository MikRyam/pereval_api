from pydantic import BaseModel
from typing import List
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    """
    Позволяет автоматически конвертировать данные из БД (db.models.py)
    в данные которые мы хотим вывести в UserDisplay
    """
    username: str
    email: str
    # items: List[Article] = []
    class Config(): 
        orm_mode = True


class PostBase(BaseModel): 
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int

# For PosDisplay
class User(BaseModel):
    username: str
    email: str
    class Config(): 
        orm_mode = True


class PostDisplay(BaseModel): 
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    class Config(): 
        orm_mode = True


class UserAuth(BaseModel):
  id: int
  username: str
  email: str
  
