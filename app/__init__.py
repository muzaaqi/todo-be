from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://localhost:5173", "https://todo.muzaaqi.my.id"]}})
    JWTManager(app)

    from app.models import User
    from app.models import Todo
    from app.models import Category
    from app.models import todo_categories

    from app.routes import api
    app.register_blueprint(api)

    return app