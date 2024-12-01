from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud, models

router = APIRouter()


@router.post("/dummy-recruiters/", response_model=schemas.DummyRecruiter)
def create_dummy_recruiter(dummy: schemas.DummyRecruiterCreate, db: Session = Depends(database.get_db)):
    # Check if the email is already registered
    existing_dummy = db.query(crud.models.DummyRecruiter).filter(crud.models.DummyRecruiter.email == dummy.email).first()
    if existing_dummy:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_dummy_recruiter(db, dummy)

@router.get("/dummy-recruiters/{dummy_recruiter_id}", response_model=schemas.DummyRecruiter)
def get_dummy_recruiter(dummy_recruiter_id: int, db: Session = Depends(database.get_db)):
    dummy_recruiter = db.query(models.DummyRecruiter).filter(models.DummyRecruiter.id == dummy_recruiter_id).first()
    if not dummy_recruiter:
        raise HTTPException(status_code=404, detail="Dummy recruiter not found")
    return dummy_recruiter

@router.get("/dummy-recruiters/", response_model=list[schemas.DummyRecruiter])
def get_all_dummy_recruiters(db: Session = Depends(database.get_db)):
    dummy_recruiters = db.query(models.DummyRecruiter).all()
    return dummy_recruiters