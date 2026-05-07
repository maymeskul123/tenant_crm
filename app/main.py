from fastapi import FastAPI
from app.database import Base, engine
from app.routes import tenant, order

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tenant CRM")

# Include routers
app.include_router(tenant.router, prefix="/tenants", tags=["tenants"])
app.include_router(order.router, prefix="/orders", tags=["orders"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}