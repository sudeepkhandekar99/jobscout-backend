from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..cloudinary_config import upload_image_to_cloudinary

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if the user already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Create a new user without hashing the password
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password,
        role_type=user.role_type,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/users/upload-image/")
async def upload_image(file: UploadFile = File(...), folder: str = "profile_photos"):
    try:
        image_url = upload_image_to_cloudinary(file, folder)
        return {"message": "Image uploaded successfully", "url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))