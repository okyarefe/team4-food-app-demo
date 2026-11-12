from dataclasses import dataclass


@dataclass
class Payment:
    id: int
    order_id: int
    amount: float
    status: str
    provider_ref: str
