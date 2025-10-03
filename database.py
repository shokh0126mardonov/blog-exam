# engine, LocalSession, Base larni yarating
from sqlalchemy import URL,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config

url_object = URL.create(
    drivername='postgresql+psycopg2',
    database=config.DB_NAME,
    password=config.DB_PASS,
    port = config.DB_PORT,
    username=config.DB_USER,
    host=config.DB_HOST
)

engine = create_engine(url_object)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()