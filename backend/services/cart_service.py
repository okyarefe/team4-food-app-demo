import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.cart import CartItem

logger = logging.getLogger(__name__)

_DB: dict[int, CartItem] = {}
_next_id = 1


def create_cart_item(menu_item_id: int, quantity: int) -> CartItem:
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    if menu_item_id < 0:
        raise ValueError("menu_item_id cannot be negative")
    global _next_id
    cart_item = CartItem(id=_next_id, menu_item_id=menu_item_id, quantity=quantity)
    _DB[_next_id] = cart_item
    _next_id += 1
    return cart_item


def get_cart_item(cart_item_id: int) -> CartItem | None:
    return _DB.get(cart_item_id)


def list_cart_items() -> list[CartItem]:
    return list(_DB.values())


def update_cart_item(cart_item_id: int, **changes) -> CartItem | None:
    cart_item = _DB.get(cart_item_id)
    if cart_item is None:
        return None
    for key, value in changes.items():
        if key == "id":
            continue
        setattr(cart_item, key, value)
    return cart_item


def delete_cart_item(cart_item_id: int) -> bool:
    return _DB.pop(cart_item_id, None) is not None


def add_to_cart(menu_item_id: int, quantity: int = 1) -> CartItem:
    for item in _DB.values():
        if item.menu_item_id == menu_item_id:
            item.quantity += quantity
            return item
    return create_cart_item(menu_item_id, quantity)


def cart_total(prices: dict[int, float]) -> float:
    return sum(prices[item.menu_item_id] * item.quantity for item in _DB.values())


def clear_cart() -> None:
    _DB.clear()
