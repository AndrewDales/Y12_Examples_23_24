import pytest
from math import sqrt
from polygon import Polygon, Triangle, Coord


def test_polygon():
    polygon = Polygon(
        Coord(0, 0),
        Coord(4, 0),
        Coord(4, 4),
        Coord(0, 4),
    )

    assert polygon.perimeter() == 16


def test_triangle():
    triangle = Triangle(Coord(0, 0), Coord(4, 0), Coord(0, 4))

    assert triangle.perimeter() == pytest.approx(8 + sqrt(32))
    assert triangle.area() == pytest.approx(8)
