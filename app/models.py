from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.ext.mutable import MutableList, MutableDict


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)  
    role_type = Column(String, nullable=True)

    # One-to-One relationship with UserProfile
    profile = relationship("UserProfile", back_populates="user", uselist=False)


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    bio = Column(Text, nullable=True)
    work_history = Column(MutableList.as_mutable(JSON), nullable=True)  # Use MutableList for JSON lists
    user_data = Column(MutableDict.as_mutable(JSON), nullable=True)  # Use MutableDict for JSON dictionaries

    user = relationship("User", back_populates="profile")