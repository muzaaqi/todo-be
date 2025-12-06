from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.models.user import User
from app.modules import response
from app import db

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return response.bad_request("Username already exists")

    new_user = User(
        username=username,
        password_hash=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()

    return response.created({"username": username}, "Register success")


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return response.unauthorized("Invalid username or password")

    token = create_access_token(identity=user.id)

    return response.ok({"token": token}, "Login success")


@user_bp.route("/me", methods=["GET"])
@jwt_required()
def get_profile():
    uid = get_jwt_identity()
    user = User.query.get(uid)

    return response.ok({
        "id": user.id,
        "username": user.username
    })
