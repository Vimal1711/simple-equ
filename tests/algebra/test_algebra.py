import pytest
import math
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ import algebra


@pytest.mark.parametrize(
    "base,exponent,expected",
    [
        (2, 3, 8.0),
        (2, 0, 1.0),
        (-2, 3, -8.0),
        (2, -1, 0.5),
        (0, 5, 0.0),
        (10, 2, 100.0),
        (2.5, 2, 6.25),
    ],
)
def test_power(base, exponent, expected):
    assert algebra.power(base, exponent) == pytest.approx(expected, rel=1e-9)


@pytest.mark.parametrize(
    "number,expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_positive(number, expected):
    assert algebra.factorial(number) == expected


def test_factorial_negative():
    assert algebra.factorial(-5) == 1


def test_factorial_float():
    assert algebra.factorial(3.0) == 6


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (48, 18, 6),
        (7, 5, 1),
        (0, 5, 5),
        (15, 0, 15),
        (-48, 18, 6),
        (48.0, 18, 6.0),
    ],
)
def test_gcd(a, b, expected):
    assert algebra.gcd(a, b) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        (0, 0.0),
        (1, 1.0),
        (25, 5.0),
        (2, pytest.approx(math.sqrt(2), rel=1e-9)),
    ],
)
def test_sqrt_positive(number, expected):
    assert algebra.sqrt(number) == expected


def test_sqrt_negative():
    with pytest.raises(ValueError, match="Not a real number"):
        algebra.sqrt(-1)


@pytest.mark.parametrize(
    "x,expected",
    [
        (0, 0.0),
        (8, 2.0),
        (27, 3.0),
        (-8, -2.0),
        (1.0, 1.0),
    ],
)
def test_cbrt(x, expected):
    assert algebra.cbrt(x) == pytest.approx(expected, rel=1e-9)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, -3, 2, (1.0, 2.0)),
        (1, 0, -1, (-1.0, 1.0)),
        (1, 2, 1, (-1.0, -1.0)),
    ],
)
def test_basic_quadratic(a, b, c, expected):
    root1, root2 = algebra.basic_quadratic(a, b, c)
    assert sorted([root1, root2]) == sorted(expected)


def test_basic_quadratic_zero_a():
    with pytest.raises(ZeroDivisionError):
        algebra.basic_quadratic(0, 1, 1)


@pytest.mark.parametrize(
    "a,b,c,d,expected",
    [
        (1, -6, 11, -6, [1, 2, 3]),
    ],
)
def test_basic_qubic_three_real(a, b, c, d, expected):
    roots = algebra.basic_qubic(a, b, c, d)
    real_roots = sorted([r for r in roots if isinstance(r, (int, float))])
    assert real_roots == pytest.approx(expected, rel=1e-9)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, -8, 4.0),
        (1, 0, 0.0),
        (1, -3, 3.0),
    ],
)
def test_basic_linear(a, b, expected):
    assert algebra.basic_linear(a, b) == expected


def test_basic_linear_zero_a():
    with pytest.raises(ZeroDivisionError):
        algebra.basic_linear(0, 1)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, True),
        (10, 3, False),
        (0, 5, True),
        (7, 1, True),
        (-10, 5, True),
        (10.0, 5, True),
    ],
)
def test_is_divisible(a, b, expected):
    assert algebra.is_divisible(a, b) == expected


def test_is_divisible_zero_divisor():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        algebra.is_divisible(10, 0)
