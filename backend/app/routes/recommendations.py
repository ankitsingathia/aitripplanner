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
