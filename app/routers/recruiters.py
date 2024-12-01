from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud

router = APIRouter()


@router.post("/recruiters/", response_model=schemas.Recruiter)
def create_recruiter(recruiter: schemas.RecruiterCreate, db: Session = Depends(database.get_db)):
    # Check if the email is already registered
    existing_recruiter = db.query(crud.models.Recruiter).filter(crud.models.Recruiter.email == recruiter.email).first()
    if existing_recruiter:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_recruiter(db, recruiter)
