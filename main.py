from fastapi import FastAPI
from src.db.database import Base,engine
from src.todos.model import Todo
from src.users.model import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

