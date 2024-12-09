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
        from_attributes  = True


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
        from_attributes  = True


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
        from_attributes  = True


class DummyRecruiterBase(BaseModel):
    name: str
    email: EmailStr
    password: str


class DummyRecruiterCreate(DummyRecruiterBase):
    pass


class DummyRecruiter(DummyRecruiterBase):
    id: int

    class Config:
        from_attributes  = True


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
        from_attributes  = True


class JobListingBase(BaseModel):
    job_type: str
    salary_low: str
    salary_high: str
    immigration: bool
    apply_link: str
    job_nature: str
    job_role: str


class JobListingCreate(JobListingBase):
    organization_id: int
    recruiter_id: int


class JobListing(JobListingBase):
    id: int

    class Config:
        from_attributes  = True


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
        from_attributes  = True

# HOTFIX: New schemas for job listings:from pydantic import BaseModel
from typing import List


class OrganizationForJobListing(BaseModel):
    id: int
    name: str
    description: str
    location: str
    website: str
    logo_link: str

    class Config:
        from_attributes  = True


class RecruiterForJobListing(BaseModel):
    id: int
    name: str
    email: str
    organization_id: int

    class Config:
        from_attributes  = True


class JobDetailForJobListing(BaseModel):
    id: int
    role_data: str
    apply_link: str
    company_link: str
    about_you: str
    must_do: str

    class Config:
        from_attributes  = True


class JobListingWithRelations(BaseModel):
    id: int
    job_type: str
    salary_low: str
    salary_high: str
    immigration: bool
    apply_link: str
    job_nature: str
    created: str
    organization: OrganizationForJobListing
    recruiter: RecruiterForJobListing
    job_details: list[JobDetailForJobListing]

    class Config:
        from_attributes  = True
