from datetime import datetime
from typing import List
from models.user import Admin, User, UserCollection, UserCreate, UserRole, UserUpdate


class UserRepository:
    """Repository that holds all (crud-)interactions with the user collection"""
    async def create_user(self, user: UserCreate)->User:
        """Creates a user with role=user in the database

        Args:
            user (UserCreate): the user to create

        Returns:
            User: the user in the database
        """
        new_user = User(email=user.email, password_hash=user.password_hash,
            created_on=datetime.utcnow(), updated_on=datetime.utcnow())
        return await new_user.create()
    
    async def create_admin(self, user: UserCreate)->User:
        """Creates a admin user in the database

        Args:
            user (UserCreate): the admin user to create

        Returns:
            User: the user in the database
        """
        new_admin = Admin(email=user.email, password_hash=user.password_hash,
            created_on=datetime.utcnow(), updated_on=datetime.utcnow())
        return await new_admin.create()

    async def list_users(self)->List[User]:
        """Gets a list of all users with all different roles from the database

        Returns:
            List[User]: The list of users
        """
        return await UserCollection.all().to_list()
    

    async def list_admins(self)->List[Admin]:
        """Gets all user with role=admin from the database

        Returns:
            List[Admin]: The list of admin users
        """
        return await Admin.all().to_list()

    async def update_user(self, user: User, user_update: UserUpdate)->User:
        """Updates a user in the database

        Args:
            user (User): the existing user from the database
            user_update (UserUpdate): the fields to update

        Returns:
            User: the updated user
        """
        await user.update({'$set': {**user_update.dict(), User.updated_on:datetime.utcnow()}})
        return user

    async def update_role(self, user: User, new_role: UserRole)->User:
        """Updates the role of the given user

        Args:
            user (User): the user to update the role
            new_role (UserRole): the new role

        Returns:
            User: the updated user
        """
        await user.update({'$set': {User.role: new_role}})
        return user

    async def get_user_by_email(self, email: str)->User|None:
        """gets a user by email from the database

        Args:
            email (str): the email

        Returns:
            User: the User in the database or None 
        """
        return await UserCollection.find_one({'email': email})
