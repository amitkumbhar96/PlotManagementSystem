from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas, crud
from database import SessionLocal
from routers.auth import get_current_admin

router = APIRouter(prefix="/plots", tags=["Plots"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_plots(
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):
    return crud.get_plots(db)

@router.post("/")
def add_plot(
    plot: schemas.PlotCreate,
    db: Session = Depends(get_db),
    admin: str = Depends(get_current_admin)
):
    return crud.create_plot(db, plot)
