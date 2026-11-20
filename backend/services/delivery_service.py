import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.delivery import Delivery

logger = logging.getLogger(__name__)

_DB: dict[int, Delivery] = {}
_next_id = 1


def create_delivery(order_id: int, address: str, eta_minutes: int, status: str) -> Delivery:
    global _next_id
    delivery = Delivery(id=_next_id, order_id=order_id, address=address, eta_minutes=eta_minutes, status=status)
    _DB[_next_id] = delivery
    _next_id += 1
    return delivery
