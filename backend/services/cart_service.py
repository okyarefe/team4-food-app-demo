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
    global _next_id
    cart_item = CartItem(id=_next_id, menu_item_id=menu_item_id, quantity=quantity)
    _DB[_next_id] = cart_item
    _next_id += 1
    return cart_item


def get_cart_item(cart_item_id: int) -> CartItem | None:
    return _DB.get(cart_item_id)
