import os
import unittest
from unittest.mock import patch

from app import create_app


class GenerateTripRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_missing_destination_returns_400(self):
        response = self.client.post("/api/generate-trip", json={"interests": ["food"]})

        self.assertEqual(response.status_code, 400)

    def test_missing_api_key_returns_500(self):
        with patch.dict(os.environ, {}, clear=True):
            response = self.client.post(
                "/api/generate-trip", json={"destination": "Paris", "interests": ["art"]}
            )

        self.assertEqual(response.status_code, 500)

    @patch("app.routes.recommendations.requests.post")
    def test_success_returns_trip_plan(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": '{"summary": "Great trip", "daily_plan": [], "tips": []}'}
                        ]
                    }
                }
            ]
        }

        with patch.dict(os.environ, {"GEMINI_API_KEY": "test-key"}):
            response = self.client.post(
                "/api/generate-trip",
                json={"destination": "Paris", "interests": ["art"], "duration_days": 2},
            )

        self.assertEqual(response.status_code, 200)
        self.assertIn("trip_plan", response.get_json())


if __name__ == "__main__":
    unittest.main()
