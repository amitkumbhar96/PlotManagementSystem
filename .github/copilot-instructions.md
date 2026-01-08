<!-- .github/copilot-instructions.md: Guidance for AI coding agents working on PlotManagementSystem -->
# PlotManagementSystem — AI Agent Instructions

Purpose: concise, actionable guidance to get productive in this repo quickly.

- **Big picture**: This repo contains a FastAPI backend (folder `fastapi/`) and a Python Tkinter desktop admin client (folder `desktopapp/`). The desktop client calls the backend REST API (configured in `desktopapp/utils/config.py`). The DB is a local SQLite file created at `fastapi/plot.db`.

- **Key components**:
  - **Backend** (`fastapi/`): `main.py` mounts routers from `fastapi/routers/*.py`. Models are in `fastapi/models.py`, Pydantic schemas in `fastapi/schemas.py`, persistence in `fastapi/crud.py`, DB config in `fastapi/database.py`, and auth helpers in `fastapi/auth_utils.py`.
  - **Desktop GUI** (`desktopapp/`): entry `desktopapp/main.py` → `screens/login_screen.open_login()`. API clients are implemented in `desktopapp/api_client.py`. Token storage is `desktopapp/auth_store.py`.

- **Run / debug**
  - Backend (Windows PowerShell):
    ```powershell
    cd fastapi
    .\myenv\Scripts\Activate.ps1   # or Activate.bat for cmd
    pip install -r requirements.txt  # if you need deps (fastapi, uvicorn, sqlalchemy, jose, passlib)
    uvicorn main:app --reload --host 127.0.0.1 --port 8000
    ```
  - Desktop app (Windows PowerShell):
    ```powershell
    cd desktopapp
    .\myenv\Scripts\Activate.ps1
    python main.py
    ```

- **API integration**:
  - Desktop uses `BASE_API_URL` from `desktopapp/utils/config.py` (default `http://127.0.0.1:8000`). Keep this in sync when changing backend port/host.
  - Routes use prefixes defined in routers: e.g., plots are under `/plots` (see `fastapi/routers/plots.py`), buyers `/buyers`, inquiries `/inquiries`, auth `/auth`.

- **Auth & tokens**:
  - Backend issues JWTs via `fastapi/auth_utils.py` (default `SECRET_KEY` = `CHANGE_THIS_SECRET` in dev). Tokens are expected as Bearer tokens.
  - Desktop stores token in memory via `desktopapp/auth_store.py`; `desktopapp/api_client._headers()` injects `Authorization: Bearer <token>`.

- **Project-specific conventions / patterns to follow**
  - Router functions declare a `get_db()` generator returning `SessionLocal()` and use `Depends(get_db)`; follow this pattern for new endpoints.
  - Pydantic request models live in `fastapi/schemas.py` and SQLAlchemy models in `fastapi/models.py` — map between them in `crud.py` using `Model(**pydantic.dict())`.
  - Routers require admin authentication via `get_current_admin` (returns the token string). Tests and new code should respect the `Depends(get_current_admin)` pattern.

- **Known issues and important gotchas (documented from code)**
  - `desktopapp/api_client.py`: `post_plot` references `response.raise_for_status()` but uses `res` for the request result; this will raise a NameError. Also endpoints for buy/inquiry are `POST /buyers/` and `POST /inquiries/` (see `fastapi/routers`), but `api_client.py` calls `/buy` and `/inquiry` — update to match router prefixes.
  - `desktopapp/screens/upload_plot_excel.py` uses `BASE_API_URL` but does not import it; fix by `from utils.config import BASE_API_URL`.
  - Default `SECRET_KEY` in `fastapi/auth_utils.py` is insecure; when deploying, set `SECRET_KEY` via env var.

- **Where to look for examples**
  - Create new endpoints: follow `fastapi/routers/plots.py` and `fastapi/routers/buyers.py`.
  - Data access + transactions: `fastapi/crud.py` (commit/refresh pattern).
  - Token flows: `fastapi/auth_utils.py` + `fastapi/routers/auth.py` + `desktopapp/api_client.py` + `desktopapp/auth_store.py`.
  - Desktop UI patterns: `desktopapp/screens/*.py` — note `open_*` functions create and run Tk windows.

- **Suggested quick tasks for agents**
  - Fix `desktopapp/api_client.py` variable mismatch and endpoint paths.
  - Add missing `BASE_API_URL` import to `upload_plot_excel.py` and fix `open_upload_plot_excel` button handler (currently calls `open_upload_plot_excel(root)` instead of passing callable).
  - Replace default secret in `fastapi/auth_utils.py` with mandatory env var check for production.

If anything here is unclear or you want more details about a particular file or workflow, tell me which area to expand. After confirmation I'll update this file further.
