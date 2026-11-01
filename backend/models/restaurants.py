from dataclasses import dataclass


@dataclass
class Restaurant:
    id: int
    name: str
    address: str
    opens_at: str
    closes_at: str
