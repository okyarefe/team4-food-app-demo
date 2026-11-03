import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.restaurants import Restaurant

logger = logging.getLogger(__name__)

_DB: dict[int, Restaurant] = {}
_next_id = 1


def create_restaurant(name: str, address: str, opens_at: str, closes_at: str) -> Restaurant:
    global _next_id
    restaurant = Restaurant(id=_next_id, name=name, address=address, opens_at=opens_at, closes_at=closes_at)
    _DB[_next_id] = restaurant
    _next_id += 1
    return restaurant


def get_restaurant(restaurant_id: int) -> Restaurant | None:
    return _DB.get(restaurant_id)


def list_restaurants() -> list[Restaurant]:
    return list(_DB.values())


def update_restaurant(restaurant_id: int, **changes) -> Restaurant | None:
    restaurant = _DB.get(restaurant_id)
    if restaurant is None:
        return None
    for key, value in changes.items():
        setattr(restaurant, key, value)
    return restaurant
