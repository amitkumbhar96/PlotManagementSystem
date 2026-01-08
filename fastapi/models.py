from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database import Base

class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)


class Plot(Base):
    __tablename__ = "plots"
    id = Column(Integer, primary_key=True, index=True)
    plot_number = Column(String, unique=True, index=True)
    total_area = Column(Float)
    market_value = Column(Float)
    min_sell_value = Column(Float)
    actual_sell_value = Column(Float, nullable=True)
    status = Column(String, default="AVAILABLE")


class Buyer(Base):
    __tablename__ = "buyers"
    id = Column(Integer, primary_key=True, index=True)
    plot_id = Column(Integer, ForeignKey("plots.id"))
    name = Column(String)
    address = Column(String)
    mobile = Column(String)
    email = Column(String)
    booking_date = Column(Date)
    booking_amount = Column(Float)
    sell_value = Column(Float)


class Inquiry(Base):
    __tablename__ = "inquiries"
    id = Column(Integer, primary_key=True, index=True)
    plot_id = Column(Integer, ForeignKey("plots.id"))
    name = Column(String)
    mobile = Column(String)
    email = Column(String)
    inquiry_date = Column(Date)
