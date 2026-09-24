from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.utils.settings import settings

engine = create_engine(settings.DATABASE_URL)
LocalSession = sessionmaker(bind=engine)

Base = declarative_base()

#session generator
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()



