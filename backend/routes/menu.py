from flask import Blueprint, jsonify, request

from services import menu_service as service

bp = Blueprint("menu", __name__, url_prefix="/api/menu")


def _to_json(value):
    if isinstance(value, list):
        return [_to_json(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_json(v) for k, v in value.items()}
    if hasattr(value, "__dict__"):
        return value.__dict__
    return value


@bp.post("")
def create_menu_item_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.create_menu_item(**data))), 201


@bp.get("/<int:item_id>")
def get_menu_item_route(item_id: int):
    result = service.get_menu_item(item_id)
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.get("")
def list_menu_items_route():
    return jsonify(_to_json(service.list_menu_items()))


@bp.patch("/<int:item_id>")
def update_menu_item_route(item_id: int):
    result = service.update_menu_item(item_id, **(request.get_json() or {}))
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.delete("/<int:item_id>")
def delete_menu_item_route(item_id: int):
    if not service.delete_menu_item(item_id):
        return jsonify({"error": "not found"}), 404
    return "", 204


@bp.post("/list-available")
def list_available_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.list_available(**data)))


@bp.post("/search-menu")
def search_menu_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.search_menu(**data)))


@bp.post("/items-by-category")
def items_by_category_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.items_by_category(**data)))
