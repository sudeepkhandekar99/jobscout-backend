from sqlalchemy.orm import Session
from . import models, schemas


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
