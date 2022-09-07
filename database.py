from motor.motor_asyncio import AsyncIOMotorClient
from settings import DatabaseSettings
from beanie import init_beanie
from models.user import User, Admin, UserCollection

async def initialize_database():
    """Initialized the database and beanie as ODM"""
    client = AsyncIOMotorClient(DatabaseSettings().url)
    beanie_models = [User, Admin, UserCollection]
    await init_beanie(client[DatabaseSettings().database], document_models=beanie_models)