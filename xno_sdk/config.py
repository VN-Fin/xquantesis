import os
from typing import Optional


class DatabaseConfiguration:
    def __init__(self):
        self.db_host: str = os.environ['POSTGRES_HOST']
        self.db_port: str = os.environ['POSTGRES_PORT']
        self.db_user: str = os.environ['POSTGRES_USER']
        self.db_password: str = os.environ['POSTGRES_PASSWORD']
        self.db_name: str = os.environ['POSTGRES_DB']

class RedisConfiguration:
    def __init__(self):
        self.redis_host: str = os.environ['REDIS_HOST']
        self.redis_port: int = int(os.environ['REDIS_PORT'])
        self.redis_password: str = os.environ['REDIS_PASSWORD']
        self.redis_db: int = int(os.environ.get('REDIS_DB', 0))


class XNOSettings:
    api_key: Optional[str] = None

    mode: str = "public"
    # Upstream REST API (public)
    api_base_url: str = "https://example.com/xno-api"

# Create a global settings instance
settings = XNOSettings()