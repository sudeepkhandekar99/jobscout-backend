from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database
from pydantic import BaseModel

router = APIRouter()

class SignInRequest(BaseModel):
    email: str
    password: str

@router.post("/auth/sign-in")
def sign_in(credentials: SignInRequest, db: Session = Depends(database.get_db)):
    # Retrieve the user by email
    user = db.query(models.User).filter(models.User.email == credentials.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Verify the password (plain text comparison here)
    if user.password != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Return a success response
    return {"message": "Sign-in successful", "user_id": user.id, "name": user.name, "email": user.email}
