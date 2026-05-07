from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class TenantBase(BaseModel):
    name: str
    email: EmailStr
    company_name: str
    is_active: bool = True

class TenantCreate(TenantBase):
    pass

class TenantUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    company_name: Optional[str] = None
    is_active: Optional[bool] = None

class TenantResponse(TenantBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True