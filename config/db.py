#from urllib.parse import quote_plus
from sqlalchemy import create_engine, MetaData

engine = create_engine('postgresql+psycopg2://jonas:password@localhost:5432/jonas')

meta = MetaData()

conn = engine.connect()
