from sqlalchemy import Column, Integer, String,Boolean
from src.db.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id =Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    is_complete = Column(Boolean, default=False)