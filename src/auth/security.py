from fastapi import Depends,HTTPException
from pwdlib import PasswordHash
from jose import jwt 
from datetime import datetime, timedelta, timezone
from src.utils.settings import settings
from fastapi.security import OAuth2PasswordBearer
from src.users.model import User
from src.db.database import get_db
from sqlalchemy.orm import Session

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/users/login")
password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

#verify password
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


#jwt token generation function
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp":expire})

    token = jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return token

#token verification
def verify_token(token: str = Depends(oauth2_schema), db:Session = Depends(get_db)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id = payload.get("id")
        exp = payload.get("exp")

        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code = 401, detail = "user not authorized")
        return user 
    except:
        raise HTTPException(
             status_code = 401,
             detail = "token invalid"
        )

   





