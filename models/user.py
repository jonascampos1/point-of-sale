from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR, SMALLINT, TEXT, DateTime
from typing import Optional
from pydantic import BaseModel

userTable = Table("users", meta,
                  Column("id", INTEGER, primary_key=True),
                  Column("username", VARCHAR(150)),
                  Column("password", SMALLINT),
                  Column("salt", VARCHAR(45)),
                  Column("created_at", DateTime),
                  Column("updated_at", DateTime),
                  Column("deleted_at", DateTime)
                )


class User(BaseModel):
    id: Optional[str]
    username: str
    password: int
    salt: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]