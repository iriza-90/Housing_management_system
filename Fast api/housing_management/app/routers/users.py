from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.utils.hashing import hash_password, verify_password
from app.utils.auth import create_access_token, get_current_user

router = APIRouter()

@router.post("/register/")
def register_user(username: str, email: str, password: str, role: str = "tenant", db: Session = Depends(get_db)):
    hashed_password = hash_password(password)
    user = User(username=username, email=email, hashed_password=hashed_password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created", "user_id": user.id}

@router.post("/login/")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me/")
def read_user(current_user: int = Depends(get_current_user)):
    return {"user_id": current_user}
