from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    order_number: str
    description: Optional[str] = None
    amount: float
    status: str = "pending"

class OrderCreate(OrderBase):
    tenant_id: int

class OrderUpdate(BaseModel):
    order_number: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[str] = None

class OrderResponse(OrderBase):
    id: int
    tenant_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True