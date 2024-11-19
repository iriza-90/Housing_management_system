from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Property, User
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/")
def create_property(address: str, city: str, rent: float, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Only admins can create properties
    user = db.query(User).filter(User.id == current_user).first()
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    property = Property(address=address, city=city, rent=rent, owner_id=current_user)
    db.add(property)
    db.commit()
    db.refresh(property)
    return {"message": "Property created", "property_id": property.id}

@router.get("/")
def get_properties(db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    return properties
