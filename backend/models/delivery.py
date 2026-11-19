from dataclasses import dataclass


@dataclass
class Delivery:
    id: int
    order_id: int
    address: str
    eta_minutes: int
    status: str
