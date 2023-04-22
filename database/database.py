import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

USER_DB=os.environ.get('USER_DB')
PASSWORD_DB=os.environ.get('PASSWORD_DB')
HOST_DB=os.environ.get('HOST_DB')
PORT_DB=os.environ.get('PORT_DB')
DATABASE_NAME=os.environ.get('DATABASE_NAME')
# SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{DATABASE_NAME}"
SQLALCHEMY_DATABASE_URL = f"postgresql+pg8000://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{DATABASE_NAME}"
engine = create_engine( SQLALCHEMY_DATABASE_URL)
if not database_exists(engine.url):
  create_database(engine.url)

    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()