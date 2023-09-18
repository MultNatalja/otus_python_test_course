from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(5, 78, 31),
                          (4, 50, 25)])
def test_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == f"Circle {radius}"
    assert int(c.get_area()) == area
    assert int(c.get_perimeter()) == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-5, 25, -20),
                          (0, 0, 0)])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert int(c.get_area()) == area
        assert int(c.get_perimeter()) == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    c = Circle(10)
    t = Triangle(5, 6, 7)
    assert int(c.add_area(s)) == 339
    assert int(c.add_area(r)) == 324
    assert int(c.add_area(t)) == 328
