from datetime import datetime

import pytest

from services import restaurants_service as service


def test_create_restaurant():
    restaurant = service.create_restaurant("test", "test", "test", "test")
    assert restaurant.id > 0


def test_get_restaurant():
    created = service.create_restaurant("test", "test", "test", "test")
    assert service.get_restaurant(created.id) == created


def test_delete_restaurant():
    created = service.create_restaurant("test", "test", "test", "test")
    assert service.delete_restaurant(created.id) is True
    assert service.get_restaurant(created.id) is None


def test_is_open_during_opening_hours():
    restaurant = service.create_restaurant("Testi", "Main st 1", "10:00", "22:00")
    assert service.is_open(restaurant, datetime(2026, 1, 1, 12, 0))
    assert not service.is_open(restaurant, datetime(2026, 1, 1, 23, 0))
