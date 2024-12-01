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