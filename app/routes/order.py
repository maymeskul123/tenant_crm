from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.crud import order as crud_order
from app.crud import tenant as crud_tenant

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=list[OrderResponse])
def list_orders(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)):
    orders = crud_order.get_all_orders(db, skip=skip, limit=limit)
    return orders

@router.get("/tenant/{tenant_id}", response_model=list[OrderResponse])
def get_orders_by_tenant(tenant_id: int, skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100), db: Session = Depends(get_db)):
    tenant = crud_tenant.get_tenant(db, tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    orders = crud_order.get_orders_by_tenant(db, tenant_id, skip=skip, limit=limit)
    return orders

@router.get("/{order_id}", response_model=OrderResponse)
def get_order_detail(order_id: int, db: Session = Depends(get_db)):
    order = crud_order.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.post("", response_model=OrderResponse, status_code=201)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    tenant = crud_tenant.get_tenant(db, order.tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return crud_order.create_order(db, order)

@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    updated_order = crud_order.update_order(db, order_id, order)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    deleted_order = crud_order.delete_order(db, order_id)
    if not deleted_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return None