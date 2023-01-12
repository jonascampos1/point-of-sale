from models.user import userTable
from config.db import conn
from models.user import UserM



def get_users():
    r = conn.execute(userTable.select()).fetchall()
    return r


def create_user(user: UserM):
    result = conn.execute(userTable.insert().values(user))
    return conn.execute(userTable.select().where(userTable.c.id == result.lastrowid)).first()
