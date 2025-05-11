import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = os.getenv("JWT_SECRET", "changeme")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

def create_access_token(data: dict, expires_delta: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
