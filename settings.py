from datetime import timedelta
from pydantic import BaseModel

class DatabaseSettings(BaseModel):
    """The database settings """
    hostname: str = 'localhost'
    port: int = 27017
    database: str = 'development'
    url: str = f'mongodb://{hostname}:{port}'

class AuthSettings(BaseModel):
    """The authentication settings"""
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    jwt_expire_minutes: timedelta = timedelta(minutes=30)
    jwt_algorithm: str = "HS256"