from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import app
from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base, UserMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))
    number = Column(String(128))
    datetime_created = Column(DateTime, default=datetime.datetime.now)
    
class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True)
    subject = Column(String(128))
    timezone = Column(String(128))
    frequency = Column(String(128))
    days = Column(String(128))
    status = Column(String(128))
    datetime_created = Column(DateTime, default=datetime.datetime.now)
    

#all classes before this line
Base.metadata.create_all(engine)