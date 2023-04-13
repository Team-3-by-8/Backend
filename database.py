from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

# load_dotenv(os.path.dirname(__file__))

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
ADDRESS = os.getenv('ADDRESS')
DATABASE_NAME = os.getenv('DATABASE_NAME')

SQLALCHEMY_DATABASE_URL = 'postgresql://' + \
    USER+':'+PASSWORD + '@'+ADDRESS+'/'+DATABASE_NAME

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
