from dataclasses import dataclass


@dataclass
class CartItem:
    id: int
    menu_item_id: int
    quantity: int
