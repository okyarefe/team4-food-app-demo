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
