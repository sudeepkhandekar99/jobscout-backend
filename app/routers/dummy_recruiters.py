from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud

router = APIRouter()


@router.post("/dummy-recruiters/", response_model=schemas.DummyRecruiter)
def create_dummy_recruiter(dummy: schemas.DummyRecruiterCreate, db: Session = Depends(database.get_db)):
    # Check if the email is already registered
    existing_dummy = db.query(crud.models.DummyRecruiter).filter(crud.models.DummyRecruiter.email == dummy.email).first()
    if existing_dummy:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_dummy_recruiter(db, dummy)
