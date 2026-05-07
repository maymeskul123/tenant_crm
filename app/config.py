from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@db:5432/tenant_crm"
    DEBUG: bool = False
    APP_NAME: str = "Tenant CRM API"
    
    class Config:
        env_file = ".env"

settings = Settings()