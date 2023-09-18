from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(1, 2, 2, 6),
                          (4, 6, 24, 20),
                          (100, 200, 20000, 600)])
def test_rectangle_positive(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.area == area
    assert r.perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-5, -10, 50, -30),
                          (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.area == area
        assert r.perimeter == perimeter


def test_rectangle_symbol(area=None, perimeter=None):
    with pytest.raises(ValueError):
        r = Rectangle("test", "test")
        assert r.area == area
        assert r.perimeter == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    c = Circle(10)
    t = Triangle(5, 6, 7)
    assert r.add_area(s) == 35
    assert int(r.add_area(c)) == 324
    assert int(r.add_area(t)) == 24
