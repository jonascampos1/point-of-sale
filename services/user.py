from models.user import userTable
from config.db import conn
from typing import Optional
from pydantic import BaseModel
import datetime
import bcrypt



class UserM(BaseModel):
    id: Optional[str]
    username: str
    password: int
    salt: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

def get_users():
    return conn.execute(userTable.select()).fetchall()

def create_user(user: UserM):

    # Declaring our password
    password = b'GeekPassword'
    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    password_hashed = bcrypt.hashpw(user.password, salt)

    user_new = {
        "username": user.username,
        "password": password_hashed,
        "salt": user.salt,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
        "deleted_at": user.deleted_at,
    }
    result = conn.execute(userTable.insert().values(user_new))
    return conn.execute(userTable.select().where(userTable.c.id == result.lastrowid)).first()
