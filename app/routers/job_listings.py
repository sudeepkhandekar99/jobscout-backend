from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud

router = APIRouter()


@router.post("/job-listings/", response_model=schemas.JobListing)
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
