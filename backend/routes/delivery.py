from flask import Blueprint, jsonify, request

from services import delivery_service as service

bp = Blueprint("delivery", __name__, url_prefix="/api/delivery")


def _to_json(value):
    if isinstance(value, list):
        return [_to_json(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_json(v) for k, v in value.items()}
    if hasattr(value, "__dict__"):
        return value.__dict__
    return value


@bp.post("")
def create_delivery_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.create_delivery(**data))), 201


@bp.get("/<int:item_id>")
def get_delivery_route(item_id: int):
    result = service.get_delivery(item_id)
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.get("")
def list_deliveries_route():
    return jsonify(_to_json(service.list_deliveries()))


@bp.patch("/<int:item_id>")
def update_delivery_route(item_id: int):
    result = service.update_delivery(item_id, **(request.get_json() or {}))
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.delete("/<int:item_id>")
def delete_delivery_route(item_id: int):
    if not service.delete_delivery(item_id):
        return jsonify({"error": "not found"}), 404
    return "", 204


@bp.post("/estimate-eta")
def estimate_eta_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.estimate_eta(**data)))
