from pydantic import BaseModel,Field

class UserBase(BaseModel):
    username:str
    email:str
    password:str=Field(min_length=8)

class UserBaseResponse(UserBase):
    username:str
    email:str
    id: int