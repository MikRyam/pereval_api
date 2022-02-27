from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
# from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey


from db.database import Base


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,
                index=True)  # цифра, создаётся автоматически при добавлении user, индекс тоже создаётся автоматически
    username = Column(String)
    email = Column(String)
    password = Column(String)  # пароль в любом случае буде захашен, никто его не увидет
    items = relationship("DbPost", back_populates="user")


class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("DbUser", back_populates="items")

