from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud, models

router = APIRouter()


@router.post("/job-details/", response_model=schemas.JobDetailCreate)
def create_job_detail(detail: schemas.JobDetailCreate, db: Session = Depends(database.get_db)):
    # Check if the job listing exists
    job_listing = db.query(crud.models.JobListing).filter(crud.models.JobListing.id == detail.job_listing_id).first()
    if not job_listing:
        raise HTTPException(status_code=404, detail="Job listing not found")

    return crud.create_job_detail(db, detail)

@router.get("/job-details/{job_detail_id}")
def get_job_detail(job_detail_id: int, db: Session = Depends(database.get_db)):
    job_detail = db.query(models.JobDetail).filter(models.JobDetail.job_listing_id == job_detail_id).first()
    if not job_detail:
        raise HTTPException(status_code=404, detail="Job detail not found")
    return job_detail.__dict__

@router.get("/job-details/")
def get_all_job_details(db: Session = Depends(database.get_db)):
    job_details = db.query(models.JobDetail).all()
    response = []
    for job in job_details:
        response.append(job.__dict__)
    return response