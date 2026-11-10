from datetime import datetime

import pytest

from services import auth_service as service


def test_create_user():
    user = service.create_user("student@example.com", "test", "test")
    assert user.id > 0
