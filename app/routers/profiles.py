from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud

router = APIRouter()


@router.post("/profiles/", response_model=schemas.UserProfile)
def create_profile(profile: schemas.UserProfileCreate, db: Session = Depends(database.get_db)):
    # Check if the user already has a profile
    existing_profile = crud.get_user_profile(db, user_id=profile.user_id)
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists")
    return crud.create_user_profile(db, profile)


@router.get("/profiles/{user_id}", response_model=schemas.UserProfile)
def get_profile(user_id: int, db: Session = Depends(database.get_db)):
    profile = crud.get_user_profile(db, user_id=user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
