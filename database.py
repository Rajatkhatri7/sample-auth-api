from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.settings import settings

POSTGRES_USER = settings.db.POSTGRES_USER
POSTGRES_PASS = settings.db.POSTGRES_PASSWORD
POSTGRES_HOST = settings.db.POSTGRES_HOST
DB = settings.db.POSTGRES_NAME

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}/{DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
