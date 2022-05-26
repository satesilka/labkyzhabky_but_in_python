from two_dimensional.two_dimens import TwoDimensionalFigure
from math import pi


class Circle(TwoDimensionalFigure):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2