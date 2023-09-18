from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(5, 6, 7, 14, 18),
                          (10, 8, 7, 27, 25)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle {side_a}, {side_b} and {side_c}"
    assert int(t.area) == area
    assert t.perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(-5, -6, -7, 14, -18),
                          (0, 0, 0, 0, 0)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
        assert int(t.area) == area
        assert t.perimeter == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    c = Circle(10)
    t = Triangle(5, 6, 7)
    assert int(t.add_area(s)) == 39
    assert int(t.add_area(c)) == 328
    assert int(t.add_area(r)) == 24
