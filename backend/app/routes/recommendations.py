import os

import requests
from flask import Blueprint, request

recommendations_bp = Blueprint("recommendations", __name__)


@recommendations_bp.post("/recommendations")
def get_recommendations():
    payload = request.get_json(silent=True) or {}

    destination = payload.get("destination", "Unknown destination")
    interests = payload.get("interests", [])

    mocked_response = {
        "destination": destination,
        "recommendations": [
            {
                "title": f"Top attractions in {destination}",
                "description": "Explore landmarks, local neighborhoods, and hidden gems.",
            },
            {
                "title": "Personalized activity plan",
                "description": (
                    f"Activities curated around your interests: {', '.join(interests) or 'general travel'}."
                ),
            },
        ],
    }

    return mocked_response, 200


@recommendations_bp.post("/generate-trip")
def generate_trip():
    payload = request.get_json(silent=True) or {}

    destination = payload.get("destination", "").strip()
    interests = payload.get("interests", [])
    duration_days = payload.get("duration_days", 3)

    if not destination:
        return {"error": "destination is required"}, 400

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY is not configured"}, 500

    interests_text = ", ".join(interests) if isinstance(interests, list) else str(interests)
    prompt = (
        "Create a concise travel itinerary in JSON with keys: summary, daily_plan, tips. "
        f"Destination: {destination}. Duration: {duration_days} days. Interests: {interests_text or 'general'}"
    )

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
        params={"key": api_key},
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=30,
    )

    if response.status_code >= 400:
        return {
            "error": "Gemini API request failed",
            "details": response.text,
        }, 502

    data = response.json()
    text = (
        data.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text", "")
    )

    if not text:
        return {"error": "Gemini API returned an empty response"}, 502

    return {
        "destination": destination,
        "duration_days": duration_days,
        "trip_plan": text,
        "model": "gemini-1.5-flash",
    }, 200
