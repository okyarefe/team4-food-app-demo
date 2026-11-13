from datetime import datetime

import pytest

from services import cart_service as service


def test_get_cart_item_missing_returns_none():
    assert service.get_cart_item(999_999) is None
