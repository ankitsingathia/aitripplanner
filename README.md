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
export GEMINI_API_KEY="your_api_key"
python run.py
```

## Backend API

- `GET /health` - health check.
- `POST /api/recommendations` - mocked recommendation response.
- `POST /api/generate-trip` - generates an itinerary via Gemini API.

Example request for `/api/generate-trip`:

```json
{
  "destination": "Tokyo",
  "interests": ["food", "temples", "nightlife"],
  "duration_days": 4
}
```

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

The React app proxies `/api` requests to the Flask backend on `http://localhost:5000`.
