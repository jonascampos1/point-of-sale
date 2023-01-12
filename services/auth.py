from models.user import UserM, userTable
from config.db import conn

def auth_user(username, password):
    res = conn\
        .execute(userTable
        .select()
        .where(userTable.c.username == username)).first()
    if res == None:
        return 0
    else:
        salt = res.salt
        print(salt)
    return res