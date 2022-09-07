"""Endpoints related to user management"""
from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from models.user import User, Admin, UserCreate, UserRead, UserRole, UserUpdate
from repositories.user import UserRepository
from security.auth import INSUFFICIENT_PERMISSIONS_ERROR, AuthRules

router = APIRouter()

async def get_user_by_email(email: str)->User:
    """Gets the user from the database

    Args:
        email (str): the email of the user

    Raises:
        HTTPException: with status 404 if not found

    Returns:
        User: the user in the database
    """
    user = await UserRepository().get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The user with email {email} does not exist')
    return user

async def get_edit_user(is_admin: bool = Depends(AuthRules.is_admin), current_user: User = Depends(AuthRules.require_user), user: User = Depends(get_user_by_email)):
    """dependency to check wheter the current user can edit the edit user

    Args:
        is_admin (bool, optional): boolean indicating if the current user is an admin. Defaults to Depends(AuthRules.is_admin).
        current_user (User, optional): the current user. Defaults to Depends(AuthRules.require_user).
        user (User, optional): the user to edit. Defaults to Depends(get_user_by_email).

    Raises:
        INSUFFICIENT_PERMISSIONS_ERROR: when the current user is neither an admin nor the user to edit

    Returns:
        User: the user to edit
    """
    if not is_admin and not user.email == current_user.email:
        raise INSUFFICIENT_PERMISSIONS_ERROR
    return user

@router.post('', response_model=UserRead)
async def create_user(user: UserCreate)->User:
    return await UserRepository().create_user(user)

@router.get('', response_model=List[UserRead])
async def list_users():
    return await UserRepository().list_users()

@router.patch('/{email}', response_model=UserRead)
async def patch_user(user_update: UserUpdate, user: User = Depends(get_edit_user)):
    return await UserRepository().update_user(user, user_update)

@router.patch('/{email}/role', response_model=User, dependencies=[(Depends(AuthRules.require_admin))])
async def patch_role(new_role: UserRole, user: User = Depends(get_edit_user)):
    return await UserRepository().update_role(user, new_role)
    

@router.post('/admins', response_model=Admin, dependencies=[Depends(AuthRules.require_admin)])
async def create_admin(user: UserCreate):
    return await UserRepository().create_admin(user)

@router.get('/admins', response_model=List[UserRead])
async def list_admins():
    return await UserRepository().list_admins()
