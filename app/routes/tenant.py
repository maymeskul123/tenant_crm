from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import tenant as crud
from app.schemas.tenant import TenantCreate, TenantUpdate, TenantResponse

router = APIRouter()

@router.post("/", response_model=TenantResponse)
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    return crud.create_tenant(db, tenant)

@router.get("/", response_model=list[TenantResponse])
def list_tenants(db: Session = Depends(get_db)):
    return crud.get_tenants(db)

@router.get("/{tenant_id}", response_model=TenantResponse)
def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
    result = crud.get_tenant(db, tenant_id)
    if not result:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return result

@router.put("/{tenant_id}", response_model=TenantResponse)
def update_tenant(tenant_id: int, tenant: TenantUpdate, db: Session = Depends(get_db)):
    result = crud.update_tenant(db, tenant_id, tenant)
    if not result:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return result

@router.delete("/{tenant_id}")
def delete_tenant(tenant_id: int, db: Session = Depends(get_db)):
    result = crud.delete_tenant(db, tenant_id)
    if not result:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return {"message": "Tenant deleted successfully", "id": result.id}