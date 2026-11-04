from datetime import datetime

import pytest

from services import menu_service as service


def test_create_menu_item():
    menu_item = service.create_menu_item("test", 9.5, "test", True)
    assert menu_item.id > 0
