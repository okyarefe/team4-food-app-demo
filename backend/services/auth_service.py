import hashlib
import logging
import os
import uuid
from datetime import datetime

from models.auth import User

logger = logging.getLogger(__name__)

_DB: dict[int, User] = {}
_next_id = 1


def create_user(email: str, password_hash: str, name: str) -> User:
    logger.info("create_user called")
    global _next_id
    user = User(id=_next_id, email=email, password_hash=password_hash, name=name)
    _DB[_next_id] = user
    _next_id += 1
    return user


def get_user(user_id: int) -> User | None:
    return _DB.get(user_id)


# TODO: add pagination
