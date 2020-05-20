import json
from random import randint, seed


class TwoNode:
    def __init__(self, key):
        self.parent = None
        self.key_left = key
        self.tree_left = None
        self.tree_right = None

    def is_3_tree(self):
        return False

    def has_child(self):
        return self.tree_left is not None or self.tree_right is not None

    def traverse(self, key):
        if not self.has_child():
            raise "Trying to traverse a leaf node: {}".format(self)
        print("Traversing Node: {}".format(self))
        if key < self.key_left:
            print("To Left: {}".format(self.tree_left))
            return (-1, True)
        if key == self.key_left:
            print("Found: {}".format(self))
            return (0, False)
        if key > self.key_left:
            print("To Right: {}".format(self.tree_right))
            return (1, True)

    def __repr__(self):
        str_to_print = "L:{}".format(self.key_left)
        if self.tree_left is not None:
            str_to_print = "{} :: LT: {}".format(str_to_print, self.tree_left)
        if self.tree_right is not None:
            str_to_print = "{} :: RT: {}".format(str_to_print, self.tree_right)
        return str_to_print
