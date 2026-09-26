from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False

class TodoResponse(TodoBase):
    title:str
    description:str
    is_completed: bool

# Data received when updating a todo
class TodoUpdate(BaseModel):
    title: str
    description: str
    is_completed: bool