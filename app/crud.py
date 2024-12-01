from sqlalchemy.orm import Session
from . import models, schemas

# user operations
def create_user_profile(db: Session, profile: schemas.UserProfileCreate):
    db_profile = models.UserProfile(
        user_id=profile.user_id,
        bio=profile.bio,
        work_history=[item.dict() for item in profile.work_history] if profile.work_history else None,
        user_data=profile.user_data.dict() if profile.user_data else None,
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_user_profile(db: Session, user_id: int):
    return db.query(models.UserProfile).filter(models.UserProfile.user_id == user_id).first()


# job operations
from sqlalchemy.orm import Session
from . import models, schemas


from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


def create_organization(db: Session, org: schemas.OrganizationCreate):
    # Check if an organization with the same name already exists
    existing_org = db.query(models.Organization).filter(models.Organization.name == org.name).first()
    if existing_org:
        raise HTTPException(status_code=400, detail="Organization with this name already exists")
    
    # Create the organization if it doesn't exist
    db_org = models.Organization(
        name=org.name,
        description=org.description,
        location=org.location,
        website=org.website,
        logo_link=org.logo_link,
    )
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org


def create_dummy_recruiter(db: Session, dummy: schemas.DummyRecruiterCreate):
    db_dummy = models.DummyRecruiter(name=dummy.name, email=dummy.email, password=dummy.password)
    db.add(db_dummy)
    db.commit()
    db.refresh(db_dummy)
    return db_dummy


def create_recruiter(db: Session, recruiter: schemas.RecruiterCreate):
    db_recruiter = models.Recruiter(
        name=recruiter.name,
        email=recruiter.email,
        password=recruiter.password,
        organization_id=recruiter.organization_id,
    )
    db.add(db_recruiter)
    db.commit()
    db.refresh(db_recruiter)
    return db_recruiter


def create_job_listing(db: Session, job: schemas.JobListingCreate):
    db_job = models.JobListing(
        organization_id=job.organization_id,
        recruiter_id=job.recruiter_id,
        job_type=job.job_type,
        salary_low=job.salary_low,
        salary_high=job.salary_high,
        immigration=job.immigration,
        apply_link=job.apply_link,
        job_nature=job.job_nature,
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def create_job_detail(db: Session, detail: schemas.JobDetailCreate):
    db_detail = models.JobDetail(
        job_listing_id=detail.job_listing_id,
        role_data=detail.role_data,
        apply_link=detail.apply_link,
        company_link=detail.company_link,
        about_you=detail.about_you,
        must_do=detail.must_do,
    )
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail
