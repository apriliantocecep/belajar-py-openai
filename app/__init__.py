from flask import Flask, jsonify
import openai
from app.routes import blueprint


def create_app() -> Flask:
    # Init Flask application
    app = Flask(__name__)

    # Set OpenAI key
    openai.api_key = "YOUR OPENAI API KEY"

    # Register the blueprints here
    register_blueprints(app)

    # Register error handlers
    register_error_handlers(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(blueprint=blueprint)


def register_error_handlers(app: Flask):
    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({"error": "Not Found"})
