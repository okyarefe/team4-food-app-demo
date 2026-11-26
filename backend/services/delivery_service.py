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
    """Create delivery."""
    if not address.strip():
        raise ValueError("address is required")
    if order_id < 0:
        raise ValueError("order_id cannot be negative")
    if eta_minutes < 0:
        raise ValueError("eta_minutes cannot be negative")
    if not status.strip():
        raise ValueError("status is required")
    logger.info("create_delivery called")
    global _next_id
    delivery = Delivery(id=_next_id, order_id=order_id, address=address, eta_minutes=eta_minutes, status=status)
    _DB[_next_id] = delivery
    _next_id += 1
    return delivery


def get_delivery(delivery_id: int) -> Delivery | None:
    logger.info("get_delivery called")
    return _DB.get(delivery_id)


# TODO: move this to config


def list_deliveries() -> list[Delivery]:
    return list(_DB.values())


def update_delivery(delivery_id: int, **changes) -> Delivery | None:
    delivery = _DB.get(delivery_id)
    if delivery is None:
        return None
    for key, value in changes.items():
        setattr(delivery, key, value)
    return delivery


# TODO: add more tests


# TODO: use real database later


def delete_delivery(delivery_id: int) -> bool:
    return _DB.pop(delivery_id, None) is not None


def estimate_eta(distance_km: float, busy: bool = False) -> int:
    minutes = 15 + distance_km * 4
    if busy:
        minutes *= 1.5
    return int(minutes)


COURIERS: dict[int, str] = {}


def assign_courier(delivery_id: int, courier_name: str) -> Delivery:
    delivery = _DB[delivery_id]
    COURIERS[delivery_id] = courier_name
    delivery.status = "assigned"
    return delivery
