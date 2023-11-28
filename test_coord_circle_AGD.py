import pytest
from math import sqrt

from coord_circle_AGD import Coord, Circle


class TestCoord:

    @pytest.fixture
    def points(self):
        coords = [Coord(-2, 4),
                  Coord(14, 6),
                  Coord(0, -4)]
        return coords

    def test_distance(self, points):
        assert points[0].distance(points[1]) == pytest.approx(sqrt(16**2 + 2**2))
        assert points[0].distance(points[2]) == pytest.approx(8.25, abs=0.005)



class TestCircle:
    @pytest.fixture
    def circles(self):
        return [Circle(Coord(0, 0), 5),
                Circle(Coord(3, 6), 7),
                Circle(Coord(5, 2), 4),
                ]

    def test_area(self, circles):
        assert circles[0].area() == pytest.approx(78.53, rel=0.0001)
        assert circles[1].area() == pytest.approx(153.93804)
        assert circles[2].area() == pytest.approx(50.26548246)

    def test_perimeter(self, circles):
        assert circles[0].perimeter() == pytest.approx(31.41592654)
        assert circles[1].perimeter() == pytest.approx(43.98229715)
        assert circles[2].perimeter() == pytest.approx(25.13274123)

    def test_inside(self, circles):
        assert not circles[0].inside(Coord(7, 6))
        assert circles[1].inside(Coord(5, 5))
        assert circles[2].inside(Coord(5, 6))
