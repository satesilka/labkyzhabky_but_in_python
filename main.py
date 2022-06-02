from Student import Student
from Node import Node


def main():
    first = Student("Styles", "Harry", "MU - 41", 1994, 87)
    second = Student("Sternenko", "Serhiy", "MP - 32", 1995, 95)
    third = Student("Markus", "Valeriy", "PO - 23", 1993, 90)
    fourth = Student("Hadid", "Gigi", "MO-11", 1995, 89)

    root = Node(first)
    root.insert(second)
    root.insert(third)
    root.insert(fourth)
    root.print()
    root.print_by_rating(88)
    root.remove_by_group("MO-11")
    root.print()


if __name__ == "__main__":
    main()
