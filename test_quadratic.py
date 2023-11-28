from quadratic import quadratic
from math import sqrt
import pytest


class TestNormal:
    def test_quadratic(self):
        assert quadratic(1, -3, -2) == (1, 2)
        assert quadratic(1, 5, 6) == (-3, -2)

    def test_quadratic_float(self):
        assert quadratic(1, 0, -2) == pytest.approx((-1.14121356, 1.14121356))
