from fastapi import FastAPI
from .routers import users
from .database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include user routes
app.include_router(users.router, prefix="/users", tags=["users"])
