import math

from src.figures.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Any side must be more than 0")
        if side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a:
            raise ValueError("Can't create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a}, {side_b} and {side_c}"
        super().__init__()

    def get_area(self):
        s = self.perimeter / 2
        d = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return d

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
