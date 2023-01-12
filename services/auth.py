from models.user import UserM, userTable
from config.db import conn
import hashlib


def auth_user(username, password):
    res = conn \
        .execute(userTable
                 .select()
                 .where(userTable.c.username == username))\
        .first()
    if res == None:
        return 0
    else:
        salt = res.salt
        password_hashed = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
        res = conn \
            .execute(userTable
                     .select()
                     .where(userTable.c.username == username)
                     .where(userTable.c.password == password_hashed))\
            .first()
        if res is not None:
            return 1
        else:
            return 0

