import pytest


@pytest.mark.parametrize(
    ('x', 'y', 'result'),
    [
        (1, 2, 3),
        (3, 4, 7),
        (5, 6, 11)
    ]
)
def test_add(x: int, y: int, result: int) -> None:
    assert x + y == result, "Неверный ответ!"


@pytest.mark.parametrize('x', [1, 2, 3])
@pytest.mark.parametrize('y', [-1, 0, 4])
def test_sum(x: int, y: int) -> None:
    assert x + y >= 0, "Неверный ответ!"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        pytest.param(
            "6*9", 42, marks=pytest.mark.xfail
        )
    ]
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
