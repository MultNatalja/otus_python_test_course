from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(1, 1, 4),
                          (4, 16, 16),
                          (100, 10000, 400)])
def test_square(side_a, area, perimeter):
    s = Square(side_a)
    assert s.name == f"Square {side_a}"
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(-5, 25, -20),
                          (0, 0, 0)])
def test_square_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        s = Square(side_a)
        assert s.get_area() == area
        assert s.get_perimeter() == perimeter


def test_square_symbol(area=None, perimeter=None):
    with pytest.raises(ValueError):
        s = Square("test")
        assert s.get_area() == area
        assert s.get_perimeter() == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    c = Circle(10)
    t = Triangle(5, 6, 7)
    assert s.add_area(r) == 35
    assert int(s.add_area(c)) == 339
    assert int(s.add_area(t)) == 39
