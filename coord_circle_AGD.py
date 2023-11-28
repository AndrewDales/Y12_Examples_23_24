import numpy
import math


class Coord:
    def __init__(self, x, y):
        self.point = numpy.array((x, y))

    def __abs__(self):
        return math.sqrt(self.point[0] ** 2 + self.point[1] ** 2)

    def distance(self, other: 'Coord'):
        diff = self.point - other.point
        coord_diff = Coord(diff[0], diff[1])
        return abs(coord_diff)

    def __repr__(self):
        return f"Coord({self.point[0]}, {self.point[1]})"


class Circle:
    def __init__(self, centre: Coord, radius: int):
        self.centre = centre
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * 2 * self.radius

    def inside(self, coord):
        return self.centre.distance(coord) <= self.radius

    def __repr__(self):
        return f"Circle(centre = {self.centre}, radius = {self.radius})"


if __name__ == "__main__":
    my_circle = Circle(Coord(3, 4), 5)
