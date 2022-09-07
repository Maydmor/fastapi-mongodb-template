from fastapi import FastAPI
from database import initialize_database
from routers.user import router as user_router
from routers.auth import router as auth_router

app = FastAPI()

app.include_router(user_router, prefix='/users', tags=['Users'])
app.include_router(auth_router, tags=['Security'])
@app.on_event('startup')
async def on_startup():
    await initialize_database()

