from two_dimensional.two_dimens import TwoDimensionalFigure


class Rectangle(TwoDimensionalFigure):
    def __init__(self, a: int, b:int):
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b