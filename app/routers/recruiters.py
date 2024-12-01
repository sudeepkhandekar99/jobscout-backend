from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud, models

router = APIRouter()


@router.post("/recruiters/", response_model=schemas.Recruiter)
def create_recruiter(recruiter: schemas.RecruiterCreate, db: Session = Depends(database.get_db)):
    # Check if the email is already registered
    existing_recruiter = db.query(crud.models.Recruiter).filter(crud.models.Recruiter.email == recruiter.email).first()
    if existing_recruiter:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_recruiter(db, recruiter)

@router.get("/recruiters/{recruiter_id}", response_model=schemas.Recruiter)
def get_recruiter(recruiter_id: int, db: Session = Depends(database.get_db)):
    recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == recruiter_id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter not found")
    return recruiter

@router.get("/recruiters/", response_model=list[schemas.Recruiter])
def get_all_recruiters(db: Session = Depends(database.get_db)):
    recruiters = db.query(models.Recruiter).all()
    return recruiters