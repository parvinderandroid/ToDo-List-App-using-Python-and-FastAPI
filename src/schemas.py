from pydantic import BaseModel


class TodoRequest(BaseModel):
    # define the fields for creating a todo item
    task: str


class TodoResponse(BaseModel):
    # define the fields for returning a todo item
    id: int
    task: str
