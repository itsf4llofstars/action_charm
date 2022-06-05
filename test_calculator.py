from main import add_num
from main import hypot


def test_add_num() -> None:
    a = 237
    b = 123
    z = add_num(a, b)
    assert z == 360


def test_hypot() -> None:
    a = 300
    b = 400
    c = hypot(a, b)
    assert c == 500

