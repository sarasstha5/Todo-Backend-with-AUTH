from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from schema.todo import TodoBase,TodoResponse
from src.db.database import get_db
from src.todos.model import Todo

router = APIRouter(prefix="/todos")

@router.post("/", response_model = TodoResponse)
def create_todo(todo:TodoBase, db:Session = Depends(get_db)):
    new_todo = Todo(
        title= todo.title,
        description=todo.description,
        is_completed = todo.is_completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

