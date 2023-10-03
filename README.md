# ToDo List App using Python FastAPI

This is a simple ToDo List application built using Python's FastAPI framework. The application provides a RESTful API for managing a list of todo items.

## Project Structure

The project is structured into several Python files:

- `database.py`: This file sets up the database engine, base class for the models, and session factory for the database operations using SQLAlchemy.
- `models.py`: This file defines the `Todo` model which represents a todo item in the database.
- `schemas.py`: This file defines the Pydantic models for the request and response data of the API endpoints.
- `main.py`: This file contains the FastAPI application and all the API endpoints.

## API Endpoints

The application provides the following API endpoints:

- `GET /`: Returns a welcome message.
- `POST /todo`: Creates a new todo item.
- `GET /todo/{id}`: Returns a todo item by its id.
- `PUT /todo/{id}`: Updates a todo item by its id.
- `DELETE /todo/{id}`: Deletes a todo item by its id.
- `GET /todo`: Returns all the todo items as a list.

## Setup and Run

To set up and run the application, follow these steps:

1. Install the required Python packages using:
```bash
pip install fastapi[all]
```
2. Run the main.py file using :
```bash
uvicorn main:app --reload
```
