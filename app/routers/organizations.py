from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, crud, models

router = APIRouter()


@router.post("/organizations/", response_model=schemas.Organization)
def create_organization(org: schemas.OrganizationCreate, db: Session = Depends(database.get_db)):
    return crud.create_organization(db, org)


@router.get("/organizations/{organization_id}", response_model=schemas.Organization)
def get_organization(organization_id: int, db: Session = Depends(database.get_db)):
    organization = db.query(models.Organization).filter(models.Organization.id == organization_id).first()
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization

@router.get("/organizations/", response_model=list[schemas.Organization])
def get_all_organizations(db: Session = Depends(database.get_db)):
    organizations = db.query(models.Organization).all()
    return organizations
