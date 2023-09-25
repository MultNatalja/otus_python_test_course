from src.figures.Rectangle import Rectangle
from src.figures.Square import Square
from src.figures.Circle import Circle
from src.figures.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(5, 78, 31)])
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
        Circle(radius)


@pytest.mark.parametrize(("first_figure", "second_figure", "summ_area"),
                         [(Circle(10), Square(5), 339),
                         (Circle(10), Rectangle(2, 5), 324),
                         (Circle(10), Triangle(5, 6, 7), 328)])
def test_add_area(first_figure, second_figure, summ_area):
    assert int(first_figure.add_area(second_figure)) == summ_area
