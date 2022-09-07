from datetime import datetime
import enum
from typing import Optional
from beanie import UnionDoc, Document, Indexed, Replace, before_event, Insert
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCollection(UnionDoc):
    """ The collection holding all User Documents"""
    class Settings:
        collection_name = 'user_collection'

class UserRole(enum.Enum):
    """All available User Roles, extend this to add a new role"""
    admin = 'admin'
    user = 'user'

class UserCreate(BaseModel):
    """Model for user creation"""
    email: EmailStr
    password: str
    @property
    def password_hash(self):
        return pwd_context.hash(self.password)

class NameInfo(BaseModel):
    """Model for name info of the person behind a user"""
    firstname: str
    lastname: str

class UserUpdate(BaseModel):
    """Model for patching a user"""
    name: Optional[NameInfo]

class UserRead(BaseModel):
    """Model that is returned on api requests. Add the fields you want to show"""
    email: EmailStr
    name: Optional[NameInfo]
    role: UserRole

class User(Document):
    """Database model for Users, inherit from this class to create a specialized type of user"""
    email: Indexed(EmailStr, unique=True)
    name: Optional[NameInfo]
    password_hash: str
    role: UserRole = UserRole.user
    created_on: datetime
    updated_on: datetime

    @property
    def is_admin(self)->bool:
        return self.role == UserRole.admin

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @before_event([Replace, Insert])
    def update_timestamp(self):
        self.updated_on = datetime.utcnow()
    class Settings:
        union_doc = UserCollection


class Admin(User):
    """Admin user model"""
    role = UserRole.admin