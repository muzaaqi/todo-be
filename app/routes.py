from flask import Blueprint
from app.controllers.user_controller import user_bp
from app.controllers.todo_controller import todo_bp

api = Blueprint("api", __name__, url_prefix="/api")

api.register_blueprint(user_bp)
api.register_blueprint(todo_bp)
