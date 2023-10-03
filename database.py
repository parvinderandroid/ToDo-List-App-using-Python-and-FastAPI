from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a database engine using SQLite
engine = create_engine("sqlite:///ToDo.db")
# create a base class for the models
Base = declarative_base()
# create a session factory for the database operations
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
