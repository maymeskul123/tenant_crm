from sqlalchemy.orm import Session
from app.models.tenant import Tenant
from app.schemas.tenant import TenantCreate, TenantUpdate

def create_tenant(db: Session, tenant: TenantCreate):
    db_tenant = Tenant(**tenant.dict())
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

def get_tenants(db: Session):
    return db.query(Tenant).all()

def get_tenant(db: Session, tenant_id: int):
    return db.query(Tenant).filter(Tenant.id == tenant_id).first()

def update_tenant(db: Session, tenant_id: int, tenant: TenantUpdate):
    db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if db_tenant:
        update_data = tenant.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_tenant, key, value)
        db.commit()
        db.refresh(db_tenant)
    return db_tenant

def delete_tenant(db: Session, tenant_id: int):
    db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if db_tenant:
        db.delete(db_tenant)
        db.commit()
    return db_tenant