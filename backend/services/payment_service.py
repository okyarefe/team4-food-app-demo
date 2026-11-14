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
