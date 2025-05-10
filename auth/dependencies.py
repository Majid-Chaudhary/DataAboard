from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import List, Optional

SECRET_KEY = "your-super-secret"  # Use .env in real use
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        groups: Optional[List[str]] = payload.get("groups", [])

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid JWT payload")

        return {"username": username, "groups": groups}

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def require_roles(required: List[str]):
    def _check(user: dict = Depends(get_current_user)):
        user_groups = user.get("groups", [])
        if not any(role in user_groups for role in required):
            raise HTTPException(
                status_code=403,
                detail=f"Requires one of roles: {required}"
            )
        return user
    return _check
