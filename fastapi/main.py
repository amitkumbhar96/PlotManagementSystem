from fastapi import FastAPI
from database import engine
import models

from routers import auth, plots, buyers, inquiries

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Plot Management API")

app.include_router(auth.router)
app.include_router(plots.router)
app.include_router(buyers.router)
app.include_router(inquiries.router)
