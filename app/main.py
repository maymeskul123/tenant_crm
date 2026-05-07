from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import Base, engine
from app.routes import tenant, order

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="Multi-tenant CRM API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Включение routes
app.include_router(tenant.router)
app.include_router(order.router)

@app.get("/", tags=["health"])
def read_root():
    return {"message": "Tenant CRM API", "status": "running"}

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy"}