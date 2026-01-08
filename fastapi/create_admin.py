from database import SessionLocal, engine
from models import Admin, Base
from auth_utils import hash_password

Base.metadata.create_all(bind=engine)

db = SessionLocal()

admin = Admin(
    username="admin",
    password_hash=hash_password("admin123")
)

db.add(admin)
db.commit()
db.close()

print("Admin user created")
