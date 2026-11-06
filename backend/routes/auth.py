from flask import Blueprint, jsonify, request

from services import auth_service as service

bp = Blueprint("auth", __name__, url_prefix="/api/auth")


def _to_json(value):
    if isinstance(value, list):
        return [_to_json(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_json(v) for k, v in value.items()}
    if hasattr(value, "__dict__"):
        return value.__dict__
    return value


@bp.post("")
def create_user_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.create_user(**data))), 201


@bp.get("/<int:item_id>")
def get_user_route(item_id: int):
    result = service.get_user(item_id)
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.get("")
def list_users_route():
    return jsonify(_to_json(service.list_users()))


@bp.patch("/<int:item_id>")
def update_user_route(item_id: int):
    result = service.update_user(item_id, **(request.get_json() or {}))
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.delete("/<int:item_id>")
def delete_user_route(item_id: int):
    if not service.delete_user(item_id):
        return jsonify({"error": "not found"}), 404
    return "", 204


@bp.post("/hash-password")
def hash_password_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.hash_password(**data)))


@bp.post("/verify-password")
def verify_password_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.verify_password(**data)))


@bp.post("/register-user")
def register_user_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.register_user(**data)))
