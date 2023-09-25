from src.figures.Rectangle import Rectangle
from src.figures.Square import Square
from src.figures.Circle import Circle
from src.figures.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20)])
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
        Rectangle(side_a, side_b)


def test_rectangle_symbol():
    with pytest.raises(ValueError):
        Rectangle("test", "test")


@pytest.mark.parametrize(("first_figure", "second_figure", "summ_area"),
                         [(Rectangle(2, 5), Triangle(5, 6, 7), 24),
                          (Rectangle(2, 5), Square(5), 35),
                          (Rectangle(2, 5), Circle(10), 324)])
def test_add_area(first_figure, second_figure, summ_area):
    assert int(first_figure.add_area(second_figure)) == summ_area
