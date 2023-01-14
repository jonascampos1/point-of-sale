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
        if username == res.username and password_hashed == res.password:
            return 1

