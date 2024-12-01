from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud

router = APIRouter()


@router.post("/job-details/", response_model=schemas.JobDetail)
def create_job_detail(detail: schemas.JobDetailCreate, db: Session = Depends(database.get_db)):
    # Check if the job listing exists
    job_listing = db.query(crud.models.JobListing).filter(crud.models.JobListing.id == detail.job_listing_id).first()
    if not job_listing:
        raise HTTPException(status_code=404, detail="Job listing not found")

    return crud.create_job_detail(db, detail)
