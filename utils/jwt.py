from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from fastapi import HTTPException, status
from config import SECRET_KEY

# Secret and Algorithm
# SECRET_KEY = "your-secret-key"  # Use env variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def get_user_payload(token:str | None):
    token = token.credentials
    tokenPayload = verify_token(token)
    if not tokenPayload:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unathorized !!!"
            )
    return tokenPayload
