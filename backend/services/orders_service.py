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
    global _next_id
    order = Order(id=_next_id, user_id=user_id, status=status, total=total)
    _DB[_next_id] = order
    _next_id += 1
    return order
