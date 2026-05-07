"""
Tenant CRM API Application
"""

__version__ = "1.0.0"

from app.models.tenant import Tenant
from app.models.order import Order

from app.schemas.tenant import (
    TenantBase,
    TenantCreate,
    TenantUpdate,
    TenantResponse,
)
from app.schemas.order import (
    OrderBase,
    OrderCreate,
    OrderUpdate,
    OrderResponse,
)

__all__ = [
    "TenantBase", "TenantCreate", "TenantUpdate", "TenantResponse",
    "OrderBase", "OrderCreate", "OrderUpdate", "OrderResponse"
]