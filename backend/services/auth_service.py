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
    if not name.strip():
        raise ValueError("name is required")
    if not email.strip():
        raise ValueError("email is required")
    if not password_hash.strip():
        raise ValueError("password_hash is required")
    logger.info("create_user called")
    global _next_id
    user = User(id=_next_id, email=email, password_hash=password_hash, name=name)
    _DB[_next_id] = user
    _next_id += 1
    return user


def get_user(user_id: int) -> User | None:
    logger.info("get_user called")
    return _DB.get(user_id)


# TODO: add pagination


# TODO: check with team


def list_users() -> list[User]:
    """List users."""
    logger.info("list_users called")
    return list(_DB.values())


def update_user(user_id: int, **changes) -> User | None:
    user = _DB.get(user_id)
    if user is None:
        return None
    for key, value in changes.items():
        setattr(user, key, value)
    return user


def delete_user(user_id: int) -> bool:
    return _DB.pop(user_id, None) is not None


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return salt.hex() + ":" + digest.hex()


# TODO: move this to config


# TODO: cleanup


def verify_password(password: str, stored: str) -> bool:
    logger.info("verify_password called")
    salt_hex, digest_hex = stored.split(":")
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt_hex), 100_000)
    return digest.hex() == digest_hex


def register_user(email: str, password: str, name: str) -> User:
    if any(user.email == email for user in _DB.values()):
        raise ValueError("email already registered")
    return create_user(email, hash_password(password), name)
