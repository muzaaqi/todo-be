from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.todo import Todo
from app.modules import response
from app import db

todo_bp = Blueprint("todo", __name__, url_prefix="/todo")


@todo_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    uid = get_jwt_identity()
    todos = Todo.query.filter_by(user_id=uid).all()

    data = [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed,
        }
        for todo in todos
    ]

    return response.ok(data)


@todo_bp.route("/", methods=["POST"])
@jwt_required()
def create_todo():
    data = request.json
    uid = get_jwt_identity()

    new_todo = Todo(
        title=data.get("title"),
        description=data.get("description"),
        user_id=uid
    )

    db.session.add(new_todo)
    db.session.commit()

    return response.created({
        "id": new_todo.id,
        "title": new_todo.title
    })


@todo_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_todo(id):
    uid = get_jwt_identity()
    todo = Todo.query.filter_by(id=id, user_id=uid).first()

    if not todo:
        return response.not_found("Todo not found")

    data = request.json
    todo.title = data.get("title", todo.title)
    todo.description = data.get("description", todo.description)
    todo.completed = data.get("completed", todo.completed)

    db.session.commit()

    return response.ok({
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    }, "Todo updated")


@todo_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_todo(id):
    uid = get_jwt_identity()
    todo = Todo.query.filter_by(id=id, user_id=uid).first()

    if not todo:
        return response.not_found("Todo not found")

    db.session.delete(todo)
    db.session.commit()

    return response.ok(message="Todo deleted")
