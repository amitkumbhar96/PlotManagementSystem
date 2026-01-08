from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas, crud
from database import SessionLocal
from routers.auth import get_current_admin

router = APIRouter(prefix="/inquiries", tags=["Inquiries"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def inquiry_plot(
    inquiry: schemas.InquiryCreate,
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):
    return crud.create_inquiry(db, inquiry)
