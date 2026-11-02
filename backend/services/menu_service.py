import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.menu import MenuItem

logger = logging.getLogger(__name__)

_DB: dict[int, MenuItem] = {}
_next_id = 1


def create_menu_item(name: str, price: float, category: str, available: bool) -> MenuItem:
    global _next_id
    menu_item = MenuItem(id=_next_id, name=name, price=price, category=category, available=available)
    _DB[_next_id] = menu_item
    _next_id += 1
    return menu_item


def get_menu_item(menu_item_id: int) -> MenuItem | None:
    return _DB.get(menu_item_id)
