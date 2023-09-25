from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self):
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Can't add area")
        return self.area + other_figure.area
