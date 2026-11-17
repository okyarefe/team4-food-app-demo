from dataclasses import dataclass


@dataclass
class Review:
    id: int
    restaurant_id: int
    user_id: int
    rating: int
    comment: str
