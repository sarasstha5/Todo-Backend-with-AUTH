from sqlalchemy import Column, ForeignKey, Integer, String,Boolean
from sqlalchemy.orm import relationship
from src.db.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id =Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Foreign key to the User table
    user = relationship("User", back_populates="todos") # Relationship to the User table, can access the user associated with the todo item