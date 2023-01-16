from sqlalchemy import create_engine, MetaData

engine = create_engine('postgresql+psycopg2://jonas:password@db:5432/jonas')

meta = MetaData()

conn = engine.connect()
