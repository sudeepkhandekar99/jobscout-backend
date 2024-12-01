from fastapi import FastAPI
from .routers import users, profiles
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

@app.get("/")
def read_root():
    return {"ping": "pong"}

# Include user routes
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
