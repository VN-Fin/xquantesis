from pydantic import BaseSettings
from typing import Optional


class XNOSettings(BaseSettings):
    api_key: Optional[str] = None

    _mode: str = "P"
    # Database (internal)
    _db_dsn: Optional[str] = None
    # Redis (internal streaming)
    _redis_url: Optional[str] = None

    # Upstream REST API (public)
    api_base_url: str = "https://example.com/xno-api"

# Create a global settings instance
settings = XNOSettings()