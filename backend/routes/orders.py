from flask import Blueprint, jsonify, request

from services import orders_service as service

bp = Blueprint("orders", __name__, url_prefix="/api/orders")


def _to_json(value):
    if isinstance(value, list):
        return [_to_json(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_json(v) for k, v in value.items()}
    if hasattr(value, "__dict__"):
        return value.__dict__
    return value


@bp.post("")
def create_order_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.create_order(**data))), 201
