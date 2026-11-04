from datetime import datetime

import pytest

from services import restaurants_service as service


def test_create_restaurant():
    restaurant = service.create_restaurant("test", "test", "test", "test")
    assert restaurant.id > 0
