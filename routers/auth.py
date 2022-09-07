"""Endpoints related to security endpoints"""
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from models.auth import JWTToken
from security.auth import auth_user, create_access_token
from settings import AuthSettings

router = APIRouter()

@router.post('/token', response_model=JWTToken)
async def token_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await auth_user(form_data.username, form_data.password)
    token_data = {'sub': user.email}
    return JWTToken(access_token=create_access_token(token_data, AuthSettings().jwt_expire_minutes))
