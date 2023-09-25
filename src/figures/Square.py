from src.figures.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if not (isinstance(side_a, (int, float))):
            raise ValueError("Side must be a number")
        if side_a <= 0:
            raise ValueError("Can't create Square")
        self.side_a = side_a
        super().__init__(side_a, side_a)
        self.name = f"Square {side_a}"
