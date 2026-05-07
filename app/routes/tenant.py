from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tenant import TenantCreate, TenantUpdate, TenantResponse, TenantWithOrders
from app.crud import tenant as crud_tenant

router = APIRouter(prefix="/tenants", tags=["tenants"])

@router.get("", response_model=list[TenantResponse])
def list_tenants(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)):
    tenants = crud_tenant.get_all_tenants(db, skip=skip, limit=limit)
    return tenants

@router.get("/{tenant_id}", response_model=TenantWithOrders)
def get_tenant_detail(tenant_id: int, db: Session = Depends(get_db)):
    tenant = crud_tenant.get_tenant(db, tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

@router.post("", response_model=TenantResponse, status_code=201)
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    existing_tenant = crud_tenant.get_tenant_by_email(db, tenant.email)
    if existing_tenant:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_tenant.create_tenant(db, tenant)

@router.put("/{tenant_id}", response_model=TenantResponse)
def update_tenant(tenant_id: int, tenant: TenantUpdate, db: Session = Depends(get_db)):
    updated_tenant = crud_tenant.update_tenant(db, tenant_id, tenant)
    if not updated_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return updated_tenant

@router.delete("/{tenant_id}", status_code=204)
def delete_tenant(tenant_id: int, db: Session = Depends(get_db)):
    deleted_tenant = crud_tenant.delete_tenant(db, tenant_id)
    if not deleted_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return None