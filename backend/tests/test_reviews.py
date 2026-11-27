from datetime import datetime

import pytest

from services import reviews_service as service


def test_create_review():
    review = service.create_review(1, 1, 1, "test")
    assert review.id > 0


def test_get_review():
    created = service.create_review(1, 1, 1, "test")
    assert service.get_review(created.id) == created


def test_delete_review():
    created = service.create_review(1, 1, 1, "test")
    assert service.delete_review(created.id) is True
    assert service.get_review(created.id) is None


def test_average_rating():
    service.create_review(7, 1, 4, "good")
    service.create_review(7, 2, 2, "meh")
    assert service.average_rating(7) == 3.0
