from flask import Blueprint, jsonify, request

from services import cart_service as service

bp = Blueprint("cart", __name__, url_prefix="/api/cart")


def _to_json(value):
    if isinstance(value, list):
        return [_to_json(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_json(v) for k, v in value.items()}
    if hasattr(value, "__dict__"):
        return value.__dict__
    return value


@bp.post("")
def create_cart_item_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.create_cart_item(**data))), 201


@bp.get("/<int:item_id>")
def get_cart_item_route(item_id: int):
    result = service.get_cart_item(item_id)
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.get("")
def list_cart_items_route():
    return jsonify(_to_json(service.list_cart_items()))


@bp.patch("/<int:item_id>")
def update_cart_item_route(item_id: int):
    result = service.update_cart_item(item_id, **(request.get_json() or {}))
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.delete("/<int:item_id>")
def delete_cart_item_route(item_id: int):
    if not service.delete_cart_item(item_id):
        return jsonify({"error": "not found"}), 404
    return "", 204
