from datetime import datetime

import pytest

from services import orders_service as service


def test_create_order():
    order = service.create_order(1, "test", 9.5)
    assert order.id > 0
