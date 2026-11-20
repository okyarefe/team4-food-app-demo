import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.payment import Payment

logger = logging.getLogger(__name__)

_DB: dict[int, Payment] = {}
_next_id = 1


def create_payment(order_id: int, amount: float, status: str, provider_ref: str) -> Payment:
    global _next_id
    payment = Payment(id=_next_id, order_id=order_id, amount=amount, status=status, provider_ref=provider_ref)
    _DB[_next_id] = payment
    _next_id += 1
    return payment


def get_payment(payment_id: int) -> Payment | None:
    return _DB.get(payment_id)


def list_payments() -> list[Payment]:
    return list(_DB.values())


def create_payment_intent(order_id: int, amount: float) -> Payment:
    if amount <= 0:
        raise ValueError("amount must be positive")
    return create_payment(order_id, amount, "pending", str(uuid.uuid4()))


PROVIDER_URL = "https://api.payments.example.com/v1/confirm"


def confirm_payment(payment_id: int) -> Payment:
    import requests

    payment = _DB[payment_id]
    response = requests.post(
        PROVIDER_URL,
        json={"ref": payment.provider_ref, "amount": payment.amount},
        headers={"Authorization": f"Token {os.getenv('PAYMENT_KEY')}"},
        timeout=10,
    )
    if response.status_code == 200:
        payment.status = "confirmed"
    else:
        payment.status = "failed"
    return payment
