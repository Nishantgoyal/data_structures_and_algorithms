class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.color = 0  # Black - 0; Red - 1

    def print(self, tree):
        tree["node"] = self.key
        if self.left_child is not None:
            tree["left"] = {}
            self.left_child.print(tree["left"])
        if self.right_child is not None:
            tree["right"] = {}
            self.right_child.print(tree["right"])


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        print("\nInserting {}".format(key))
        if self.root is None:
            self.root = Node(key)
        self.print()

    def print(self):
        tree = {}
        if self.root is not None:
            self.root.print(tree)
        print(tree)
