# AI Travel Recommendation System

Project structure for an AI-powered travel recommendation system with a Flask backend and React frontend.

## Structure

- `backend/` Flask API server.
- `frontend/` React app (Vite).

## Backend setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

The React app proxies `/api` requests to the Flask backend on `http://localhost:5000`.
