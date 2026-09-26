from pydantic import BaseModel,Field

class UserBase(BaseModel):
    username:str
    email:str
    password:str=Field(min_length=8)

class UserBaseResponse(BaseModel):
    id: int
    name:str
    email:str

class Userlogin(BaseModel):
    email:str
    password:str