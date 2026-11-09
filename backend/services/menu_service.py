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
    if not category.strip():
        raise ValueError("category is required")
    if price < 0:
        raise ValueError("price cannot be negative")
    global _next_id
    menu_item = MenuItem(id=_next_id, name=name, price=price, category=category, available=available)
    _DB[_next_id] = menu_item
    _next_id += 1
    return menu_item


def get_menu_item(menu_item_id: int) -> MenuItem | None:
    """Get menu item."""
    return _DB.get(menu_item_id)


def list_menu_items() -> list[MenuItem]:
    return list(_DB.values())


def update_menu_item(menu_item_id: int, **changes) -> MenuItem | None:
    menu_item = _DB.get(menu_item_id)
    if menu_item is None:
        return None
    for key, value in changes.items():
        if key == "id":
            continue
        setattr(menu_item, key, value)
    return menu_item


def delete_menu_item(menu_item_id: int) -> bool:
    return _DB.pop(menu_item_id, None) is not None


def list_available() -> list[MenuItem]:
    return [item for item in _DB.values() if item.available]


def search_menu(query: str) -> list[MenuItem]:
    query = query.lower()
    return [item for item in _DB.values() if query in item.name.lower()]


def items_by_category() -> dict[str, list[MenuItem]]:
    """Items by category."""
    groups: dict[str, list[MenuItem]] = {}
    for item in _DB.values():
        groups.setdefault(item.category, []).append(item)
    return groups
