from flask import Blueprint, jsonify, request

from services import payment_service as service

bp = Blueprint("payment", __name__, url_prefix="/api/payment")


def _to_json(value):
    if isinstance(value, list):
        return [_to_json(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_json(v) for k, v in value.items()}
    if hasattr(value, "__dict__"):
        return value.__dict__
    return value


@bp.post("")
def create_payment_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.create_payment(**data))), 201


@bp.get("/<int:item_id>")
def get_payment_route(item_id: int):
    result = service.get_payment(item_id)
    if result is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(_to_json(result))


@bp.get("")
def list_payments_route():
    return jsonify(_to_json(service.list_payments()))


@bp.post("/create-payment-intent")
def create_payment_intent_route():
    data = request.get_json() or {}
    return jsonify(_to_json(service.create_payment_intent(**data)))
