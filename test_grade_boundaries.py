from grade_boundaries import calc_grade
import pytest


def test_calc_grade():
    assert calc_grade(255) == "A"
    assert calc_grade(188) == "C"
