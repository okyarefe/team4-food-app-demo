import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.orders import Order

logger = logging.getLogger(__name__)

_DB: dict[int, Order] = {}
_next_id = 1


def create_order(user_id: int, status: str, total: float) -> Order:
    """Create order."""
    if total < 0:
        raise ValueError("total cannot be negative")
    if user_id < 0:
        raise ValueError("user_id cannot be negative")
    global _next_id
    order = Order(id=_next_id, user_id=user_id, status=status, total=total)
    _DB[_next_id] = order
    _next_id += 1
    return order


def get_order(order_id: int) -> Order | None:
    """Get order."""
    return _DB.get(order_id)


def list_orders() -> list[Order]:
    return list(_DB.values())


def update_order(order_id: int, **changes) -> Order | None:
    order = _DB.get(order_id)
    if order is None:
        return None
    for key, value in changes.items():
        setattr(order, key, value)
    return order


def delete_order(order_id: int) -> bool:
    return _DB.pop(order_id, None) is not None
