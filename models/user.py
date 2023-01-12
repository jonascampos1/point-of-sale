from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR, SMALLINT, TEXT

userTable = Table("user", meta,
                  Column("id", INTEGER, primary_key=True),
                  Column("username", VARCHAR(150)),
                  Column("password", SMALLINT),
                  Column("salt", VARCHAR(45)),
                  Column("created_at", VARCHAR(45)),
                  Column("updated_at", TEXT),
                  Column("deleted_at", VARCHAR(2))
                  )

meta.create_all(engine)
