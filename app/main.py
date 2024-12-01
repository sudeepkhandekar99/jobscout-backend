from fastapi import FastAPI
from .routers import users, profiles, auth, organizations, dummy_recruiters, recruiters, job_listings, job_details
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
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(organizations.router, prefix="/organizations", tags=["organizations"])
app.include_router(dummy_recruiters.router, prefix="/dummy-recruiters", tags=["dummy_recruiters"])
app.include_router(recruiters.router, prefix="/recruiters", tags=["recruiters"])
app.include_router(job_listings.router, prefix="/job-listings", tags=["job_listings"])
app.include_router(job_details.router, prefix="/job-details", tags=["job_details"])
app.include_router(organizations.router, prefix="/organizations", tags=["organizations"])
app.include_router(dummy_recruiters.router, prefix="/dummy-recruiters", tags=["dummy_recruiters"])
app.include_router(recruiters.router, prefix="/recruiters", tags=["recruiters"])
app.include_router(job_listings.router, prefix="/job-listings", tags=["job_listings"])
app.include_router(job_details.router, prefix="/job-details", tags=["job_details"])