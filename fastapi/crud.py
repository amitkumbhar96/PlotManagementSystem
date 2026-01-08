from sqlalchemy.orm import Session
from models import Plot, Buyer, Inquiry, Admin

def get_admin(db: Session, username: str):
    return db.query(Admin).filter(Admin.username == username).first()


def get_plots(db: Session):
    return db.query(Plot).all()


def create_plot(db: Session, plot):
    obj = Plot(**plot.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def buy_plot(db: Session, buyer):
    plot = db.query(Plot).filter(Plot.id == buyer.plot_id).first()
    plot.status = "SOLD"
    plot.actual_sell_value = buyer.sell_value

    obj = Buyer(**buyer.dict())
    db.add(obj)
    db.commit()
    return obj


def create_inquiry(db: Session, inquiry):
    plot = db.query(Plot).filter(Plot.id == inquiry.plot_id).first()
    plot.status = "INQUIRY"

    obj = Inquiry(**inquiry.dict())
    db.add(obj)
    db.commit()
    return obj
