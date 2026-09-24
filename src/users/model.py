from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from src.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    todos = relationship("Todo", back_populates="user") # Relationship to the Todo table, can access all todo items associated with the user
