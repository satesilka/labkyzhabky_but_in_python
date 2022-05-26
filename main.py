from two_dimensional.circle import Circle
from two_dimensional.rectangle import Rectangle
from three_dimensional.sphere import Sphere
from three_dimensional.parallelepiped import Parallelepiped
from other.point import Point
from other.line_segment import LineSegment


def main():
    cir = Circle(6)
    print(cir.area)

    rect = Rectangle(5, 8)
    print(rect.area)

    sph = Sphere(3)
    print(sph.volume)
    print(sph.surface_area)

    paral = Parallelepiped(2, 4, 6)
    print(paral.volume)
    print(paral.surface_area)

    point1 = Point(1, 4, 3)
    point2 = Point(0, 2, 5)
    print(point1.x, point1.y, point1.z)
    print(point2.x, point2.y, point2.z)
    line = LineSegment(point1, point2)
    print(line.length())


if __name__ == '__main__':
    main()