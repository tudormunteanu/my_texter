from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base, engine
import datetime
from flask.ext.login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base, UserMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))
    number = Column(String(128))
    datetime_created = Column(DateTime, default=datetime.datetime.now)
    

#all classes before this line
Base.metadata.create_all(engine)