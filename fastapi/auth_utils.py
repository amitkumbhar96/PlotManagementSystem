# auth_utils.py

import os
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

# ---------------------------
# Configuration
# ---------------------------

SECRET_KEY = os.environ.get("SECRET_KEY", "CHANGE_THIS_SECRET")  # keep same default for dev
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 480  # 8 hours

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---------------------------
# Password Utilities
# ---------------------------

def hash_password(password: str) -> str:
    """Hash a plain text password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a plain text password against a hashed password."""
    return pwd_context.verify(password, hashed_password)


# ---------------------------
# JWT Token Utilities
# ---------------------------

def create_access_token(data: Dict[str, Any]) -> str:
    """
    Create a JWT access token with expiration.
    Keeps your original function signature for minimal changes.
    """
    to_encode = data.copy()  # Avoid modifying the input dictionary
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Decode a JWT token and return its payload.
    Returns None if the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
