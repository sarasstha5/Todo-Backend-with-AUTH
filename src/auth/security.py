from pwdlib import PasswordHash
from jose import jwt 
from datetime import datetime, timedelta, timezone
from src.utils.settings import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

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



   





