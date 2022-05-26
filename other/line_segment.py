from other.point import Point
from math import sqrt


class LineSegment:
    def __init__(self, begining: Point, end: Point):
        self.begining = begining
        self.end = end

    def length(self) -> float:
        return sqrt((self.begining.x - self.end.x)**2 +
                    (self.begining.y - self.end.y)**2 +
                    (self.begining.z - self.end.z)**2)