import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.reviews import Review

logger = logging.getLogger(__name__)

_DB: dict[int, Review] = {}
_next_id = 1


def create_review(restaurant_id: int, user_id: int, rating: int, comment: str) -> Review:
    global _next_id
    review = Review(id=_next_id, restaurant_id=restaurant_id, user_id=user_id, rating=rating, comment=comment)
    _DB[_next_id] = review
    _next_id += 1
    return review


def get_review(review_id: int) -> Review | None:
    return _DB.get(review_id)


def list_reviews() -> list[Review]:
    return list(_DB.values())
