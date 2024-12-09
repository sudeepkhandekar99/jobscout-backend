from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud, models
from typing import List

router = APIRouter()


@router.post("/job-listings/")
def create_job_listing(job: schemas.JobListingCreate, db: Session = Depends(database.get_db)):
    # Check if the organization exists
    organization = db.query(crud.models.Organization).filter(crud.models.Organization.id == job.organization_id).first()
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")

    # Check if the recruiter exists
    recruiter = db.query(crud.models.Recruiter).filter(crud.models.Recruiter.id == job.recruiter_id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter not found")

    return crud.create_job_listing(db, job)

@router.get("/job-listings/{job_listing_id}/detailed")
def get_detailed_job_listing(job_listing_id: int, db: Session = Depends(database.get_db)):
    job_listing = (
        db.query(models.JobListing)
        .filter(models.JobListing.id == job_listing_id)
        .first()
    )
    if not job_listing:
        raise HTTPException(status_code=404, detail="Job listing not found")

    return job_listing.__dict__

@router.get("/job-listings/detailed")
def get_all_detailed_job_listings(db: Session = Depends(database.get_db)):
    job_listings = db.query(models.JobListing).all()
    response = []
    for job in job_listings:
        response.append(job.__dict__)
    return response
