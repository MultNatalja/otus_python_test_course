from src.figures.Rectangle import Rectangle
from src.figures.Square import Square
from src.figures.Circle import Circle
from src.figures.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16)])
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
        Square(side_a)


def test_square_symbol():
    with pytest.raises(ValueError):
        Square("test")


@pytest.mark.parametrize(("first_figure", "second_figure", "summ_area"),
                         [(Square(5), Triangle(5, 6, 7), 39),
                         (Square(5), Rectangle(2, 5), 35),
                         (Square(5), Circle(10), 339)])
def test_add_area(first_figure, second_figure, summ_area):
    assert int(first_figure.add_area(second_figure)) == summ_area
