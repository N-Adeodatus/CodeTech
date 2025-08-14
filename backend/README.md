# FastAPI Backend

This backend uses MySQL (`codetech_db`) via SQLAlchemy. SQLite artifacts like `users.db` are no longer used.

## Setup

1. Create and activate a virtual environment (if not already):
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Ensure MySQL is running and the DATABASE_URL in `main.py` is correct.

4. Run the server:
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /signup` — Register a new user (email, password)
- `POST /login` — Login and get JWT token (OAuth2)
- `GET /me` — Get current user info (requires Bearer token)