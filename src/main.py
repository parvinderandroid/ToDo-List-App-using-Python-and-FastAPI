from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

# create the database tables if they do not exist
Base.metadata.create_all(engine)
# create a FastAPI app instance
app = FastAPI()


def get_session():
    # create a database session and close it after use
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    # return a welcome message for the root endpoint
    return "ToDo List App using Python FastAPI"


@app.post("/todo", response_model=schemas.TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoRequest, db: Session = Depends(get_session)):
    # create a new todo item and add it to the database
    todo_item = models.Todo(task=todo.task)
    db.add(todo_item)
    db.commit()
    return todo_item


@app.get("/todo/{id}", response_model=schemas.TodoResponse)
def read_todo(id: int, db: Session = Depends(get_session)):
    # get a todo item by its id from the database
    todo_item = db.query(models.Todo).get(id)
    if not todo_item:
        # raise an exception if the todo item is not found
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return todo_item


@app.put("/todo/{id}", response_model=schemas.TodoResponse)
def update_todo(id: int, todo: schemas.TodoRequest, db: Session = Depends(get_session)):
    # update a todo item by its id in the database
    todo_item = db.query(models.Todo).get(id)
    if todo_item:
        # change the task of the todo item and commit the changes
        todo_item.task = todo.task
        db.commit()
    if not todo_item:
        # raise an exception if the todo item is not found
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return todo_item


@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, db: Session = Depends(get_session)):
    # delete a todo item by its id from the database
    todo_item = db.query(models.Todo).get(id)
    if todo_item:
        # remove the todo item and commit the changes
        db.delete(todo_item)
        db.commit()
    else:
        # raise an exception if the todo item is not found
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return None


@app.get("/todo", response_model=List[schemas.TodoResponse])
def read_todo_list(db: Session = Depends(get_session)):
    # get all the todo items from the database as a list
    todo_list = db.query(models.Todo).all()
    return todo_list
