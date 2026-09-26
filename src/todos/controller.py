from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from src.schema.todo import TodoBase,TodoResponse, TodoUpdate
from src.db.database import get_db
from src.todos.model import Todo
from src.auth.security import verify_token

router = APIRouter(prefix="/todos")

@router.post("/todo")
def create_todo(todo:TodoBase, db:Session = Depends(get_db), user = Depends(verify_token)):
    new_todo = Todo(
        title= todo.title,
        description=todo.description,
        is_completed = todo.is_completed,
        user_id = user.id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.get("/", response_model = list[TodoResponse])
def get_todos(db:Session = Depends(get_db), user = Depends(verify_token)):
    todos = db.query(Todo).filter(Todo.user_id == user.id).all()
    return todos

@router.get("/{todo_id}", response_model = TodoResponse)
def get_todo(todo_id:int, db:Session = Depends(get_db), user = Depends(verify_token)):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}")
def put_todo(todo_id:int, todo_update:TodoUpdate, db:Session = Depends(get_db), user = Depends(verify_token)):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.title = todo_update.title
    todo.description = todo_update.description
    todo.is_completed = todo_update.is_completed

    db.commit()
    db.refresh(todo)

    return todo

@router.delete("/{todo_id}")
def delete_todo(todo_id:int, db:Session = Depends(get_db), user = Depends(verify_token)):
    todo = db.query(Todo).filter(todo_id == Todo.id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()

    return{
        "todo deleted successfully"
    }


