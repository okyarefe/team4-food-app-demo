from datetime import datetime

import pytest

from services import reviews_service as service


def test_create_review():
    review = service.create_review(1, 1, 1, "test")
    assert review.id > 0
