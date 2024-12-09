from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, DateTime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.ext.mutable import MutableList, MutableDict
from sqlalchemy.sql import func

# user models
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

# job models
class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    website = Column(String, nullable=False)
    logo_link = Column(String, nullable=False)

    recruiters = relationship("Recruiter", back_populates="organization")
    job_listings = relationship("JobListing", back_populates="organization")


class DummyRecruiter(Base):
    __tablename__ = "dummy_recruiters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Recruiter(Base):
    __tablename__ = "recruiters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    is_valid = Column(Boolean, default=False)

    organization = relationship("Organization", back_populates="recruiters")
    job_listings = relationship("JobListing", back_populates="recruiter")


class JobListing(Base):
    __tablename__ = "job_listings"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    recruiter_id = Column(Integer, ForeignKey("recruiters.id"), nullable=False)
    job_type = Column(String, nullable=False)
    salary_low = Column(String, nullable=False)
    salary_high = Column(String, nullable=False)
    immigration = Column(Boolean, default=False)
    created = Column(DateTime, server_default=func.now(), nullable=False)
    apply_link = Column(String, nullable=False)
    job_nature = Column(String, nullable=False)  # "remote", "hybrid", or default
    job_role = Column(String, nullable=False)

    organization = relationship("Organization", back_populates="job_listings")
    recruiter = relationship("Recruiter", back_populates="job_listings")
    job_details = relationship("JobDetail", back_populates="job_listing")


class JobDetail(Base):
    __tablename__ = "job_details"

    id = Column(Integer, primary_key=True, index=True)
    job_listing_id = Column(Integer, ForeignKey("job_listings.id"), nullable=False)
    role_data = Column(Text, nullable=False)
    apply_link = Column(String, nullable=False)
    company_link = Column(String, nullable=False)
    about_you = Column(Text, nullable=False)
    must_do = Column(Text, nullable=False)

    job_listing = relationship("JobListing", back_populates="job_details")