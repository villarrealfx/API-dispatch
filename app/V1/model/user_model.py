import datetime
from sqlalchemy import Date, DateTime, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from ..utils.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, autoincrement=True,
                 nullable=False)
    username = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    hiring_date = Column(Date(), nullable=False)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)

    create_at = Column(DateTime(), default=datetime.datetime.now())
    update_at = Column(DateTime(), default=datetime.datetime.now, 
                       onupdate=datetime.datetime.now)
    
    
    def __repr__(self):
        return f"User: {self.username}"