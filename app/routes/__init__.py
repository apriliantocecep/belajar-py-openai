from flask import Blueprint, jsonify
# Add Controllers
from app.controllers import main_controller

# Blueprint API v1
blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


@blueprint.get("/")
def hello():
    return "Hello World"


# change to post method
@blueprint.post("/ask")
def ask():
    # Call controller method
    return main_controller.ask()
