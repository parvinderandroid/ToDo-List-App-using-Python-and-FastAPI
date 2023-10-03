from sqlalchemy import Column, Integer, String
from database import Base


class Todo(Base):
    # define the table name for the model
    __tablename__ = "todos"
    # define the columns for the model
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
