from flask import Flask
from flask_cors import CORS

from .routes.recommendations import recommendations_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")

    CORS(app)
    app.register_blueprint(recommendations_bp, url_prefix="/api")

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    return app
