from pydantic import BaseModel
from datetime import date

# ---------- AUTH ----------
class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- PLOTS ----------
class PlotCreate(BaseModel):
    plot_number: str
    total_area: float
    market_value: float
    min_sell_value: float


class PlotResponse(BaseModel):
    id: int
    plot_number: str
    status: str

    class Config:
        from_attributes = True


# ---------- BUY ----------
class BuyerCreate(BaseModel):
    plot_id: int
    name: str
    address: str
    mobile: str
    email: str
    booking_date: date
    booking_amount: float
    sell_value: float


# ---------- INQUIRY ----------
class InquiryCreate(BaseModel):
    plot_id: int
    name: str
    mobile: str
    email: str
    inquiry_date: date
