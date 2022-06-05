from main import add_num


def test_add_num() -> None:
    a = 237
    b = 123
    z = add_num(a, b)
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert z == 360
