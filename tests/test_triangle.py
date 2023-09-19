from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(5, 6, 7, 14, 18)])
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
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(("first_figure", "second_figure", "summ_area"),
                         [(Triangle(5, 6, 7), Square(5), 39),
                         (Triangle(5, 6, 7), Rectangle(2, 5), 24),
                         (Triangle(5, 6, 7), Circle(10), 328)])
def test_add_area(first_figure, second_figure, summ_area):
    assert int(first_figure.add_area(second_figure)) == summ_area
