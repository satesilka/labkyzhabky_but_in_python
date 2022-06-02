from Student import Student


class Node:
    def __init__(self, data: Student):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: Student):
        if self.data:
            if data.rating < self.data.rating:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data.rating < data.rating:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_by_rating(self, rating: int):
        if self.left:
            self.left.print()
        if self.data and self.data.rating > rating:
            print(self.data)
        if self.right:
            self.right.print()

    def remove_by_group(self, group: str):
        if self.data and self.data.group == group:
            left = self.left
            right = self.right
            if left:
                self.data = left.data
                self.left = left.left
                self.right = left.right
                if right:
                    self.insert(right)
            elif right:
                self.data = right.data
                self.right = right.right
                self.right = right.left

        else:
            if self.left:
                self.left.remove_by_group(group)
            if self.right:
                self.right.remove_by_group(group)

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()
