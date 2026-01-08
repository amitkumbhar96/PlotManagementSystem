# api_client.py
import requests
from utils.config import BASE_API_URL
from auth_store import get_token

def _headers():
    token = get_token()
    return {
        "Authorization": f"Bearer {token}" if token else ""
    }

# ---------- AUTH ----------
def login(username, password):
    res = requests.post(
        f"{BASE_API_URL}/auth/login",
        json={  # <-- send as JSON, not 'data'
            "username": username,
            "password": password
        },
        headers={
            "Content-Type": "application/json"  # <-- JSON content type
        }
    )
    res.raise_for_status()
    return res.json()

# ---------- PLOTS ----------
def get_plots():
    res = requests.get(
        f"{BASE_API_URL}/plots",
        headers=_headers()
    )
    res.raise_for_status()
    return res.json()

#----------Add PLOTS ----------
def post_plot(payload):
    res = requests.post(
        f"{BASE_API_URL}/plots",
        json=payload,
        headers=_headers()
    )
    response.raise_for_status()
    return response.json()

# ---------- BUY ----------
def buy_plot(data):
    res = requests.post(
        f"{BASE_API_URL}/buy",
        json=data,
        headers=_headers()
    )
    res.raise_for_status()
    return res.json()

# ---------- INQUIRY ----------
def inquiry_plot(data):
    res = requests.post(
        f"{BASE_API_URL}/inquiry",
        json=data,
        headers=_headers()
    )
    res.raise_for_status()
    return res.json()
