import pytest
from sePuedeLlegar import sePuedeLlegar

@pytest.mark.parametrize(
    "parametro1, parametro2, parametro3, expected",
    [
        ("a", "b", [("c", "d"), ("a", "b"), ("v", "g")], 1),
        ("a", "b", [("c", "d"), ("a", "x"), ("v", "g")], -1),
        ("a", "b", [("c", "d"), ("a", "c"), ("c", "b")], 2),
        ("a", "d", [("b", "x"), ("a", "b"), ("b", "d")], 2),
        ("a", "b", [("c", "d"), ("r", "t"), ("v", "g")], -1),
    ]
)
def test_sePuedeLlegar(parametro1, parametro2, parametro3, expected):
    assert sePuedeLlegar(parametro1, parametro2, parametro3) == expected