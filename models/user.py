from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR, SMALLINT, TEXT

engine = create_engine("postgresql+psycopg2://jonas:password@localhost:5432/jonas")

meta = MetaData()

conn = engine.connect()



menuTabla = Table("productotemp2", meta,
                  Column("id", INTEGER, primary_key=True),
                  Column("nombre", VARCHAR(150)),
                  Column("precio", SMALLINT),
                  Column("estado", VARCHAR(45)),
                  Column("foto", VARCHAR(45)),
                  Column("descripcion", TEXT),
                  Column("tipo", VARCHAR(2)),
                  Column("tipo_foto", SMALLINT),
                  Column("rating", SMALLINT),
                  Column("comentario", TEXT),
                  Column("comentario2", TEXT)
                  )

meta.create_all(engine)
