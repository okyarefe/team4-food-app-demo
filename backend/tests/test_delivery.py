from datetime import datetime

import pytest

from services import delivery_service as service


def test_create_delivery():
    delivery = service.create_delivery(1, "test", 1, "test")
    assert delivery.id > 0
