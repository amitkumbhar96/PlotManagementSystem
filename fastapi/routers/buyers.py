from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas, crud
from database import SessionLocal
from routers.auth import get_current_admin

router = APIRouter(prefix="/buyers", tags=["Buyers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def buy_plot(
    buyer: schemas.BuyerCreate,
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):
    return crud.buy_plot(db, buyer)
