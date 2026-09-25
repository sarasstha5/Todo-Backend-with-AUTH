from fastapi import APIRouter,Depends,HTTPException
from src.schema.user import UserBase,UserBaseResponse,Userlogin
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.users.model import User 
from src.auth.security import get_password_hash,verify_password,create_token

router = APIRouter(prefix="/users")



@router.post("/register" ,response_model= UserBaseResponse)
def register(body:UserBase, db:Session = Depends(get_db)):
    is_user = db.query(User).filter(User.email == body.email).first()

    if is_user:
        raise HTTPException(
            status_code = 422,
            detail = "user already exist"
        )

    hash_password = get_password_hash(body.password)

    new_user = User(
        name = body.username,
        email = body.email,
        hashed_password = hash_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(body:Userlogin, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()
    if not user:
        raise HTTPException(
            status_code = 401,
            detail = "do not match email or password"
        )

    if not verify_password(body.password, user.hashed_password):
        raise HTTPException(
                status = 401,
                detail = "do not match email or password"
            )

    token = create_token(
        {
            "sub":user.id
        }
    )

    return {
        "access_token": token,
        "token_type" : "Bearer"
    }

    