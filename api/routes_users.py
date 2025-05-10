from fastapi import APIRouter, HTTPException
from models.user import UserLogin, TokenResponse
from auth.ldap_auth import authenticate_ldap_user
from auth.jwt_utils import create_access_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    if not authenticate_ldap_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token}
