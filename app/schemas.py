from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict

# user profile schemas
class WorkHistory(BaseModel):
    companyName: str
    role: str
    location: str
    startDate: str
    endDate: str

class UserData(BaseModel):
    currentLocation: str
    bio: Optional[str]
    linkedinLink: Optional[str]
    profileImageUrl: Optional[str]
    coverImageUrl: Optional[str]

class UserProfileBase(BaseModel):
    bio: Optional[str]
    work_history: Optional[List[WorkHistory]]
    user_data: Optional[UserData]

class UserProfileCreate(UserProfileBase):
    user_id: int

class UserProfile(UserProfileBase):
    id: int

    class Config:
        orm_mode = True


# user schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role_type: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# job schemas
class OrganizationBase(BaseModel):
    name: str
    description: str
    location: str
    website: str
    logo_link: str


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int

    class Config:
        orm_mode = True


class DummyRecruiterBase(BaseModel):
    name: str
    email: EmailStr
    password: str


class DummyRecruiterCreate(DummyRecruiterBase):
    pass


class DummyRecruiter(DummyRecruiterBase):
    id: int

    class Config:
        orm_mode = True


class RecruiterBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    organization_id: int


class RecruiterCreate(RecruiterBase):
    pass


class Recruiter(RecruiterBase):
    id: int
    is_valid: bool = False

    class Config:
        orm_mode = True


class JobListingBase(BaseModel):
    job_type: str
    salary_low: str
    salary_high: str
    immigration: bool
    apply_link: str
    job_nature: str


class JobListingCreate(JobListingBase):
    organization_id: int
    recruiter_id: int


class JobListing(JobListingBase):
    id: int

    class Config:
        orm_mode = True


class JobDetailBase(BaseModel):
    role_data: str
    apply_link: str
    company_link: str
    about_you: str
    must_do: str


class JobDetailCreate(JobDetailBase):
    job_listing_id: int


class JobDetail(JobDetailBase):
    id: int

    class Config:
        orm_mode = True