from fastapi import FastAPI
from src.db.database import Base,engine
from src.todos.model import Todo
from src.users.model import User
from src.todos.controller import router as todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router)


