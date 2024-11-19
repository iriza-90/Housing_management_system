from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Tenant
from app.utils.auth import get_current_user

router = APIRouter()

@router.get("/my-tenancy/")
def get_my_tenancy(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    tenant = db.query(Tenant).filter(Tenant.user_id == current_user).first()
    if tenant is None:
        raise HTTPException(status_code=404, detail="No tenancy found for this user")
    return tenant
