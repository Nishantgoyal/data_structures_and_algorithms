import json
from random import randint, seed


class TwoNode:
    def __init__(self, key):
        print("Creating a Two Node with key: {}".format(key))
        self.parent = None
        self.key = key
        self.tree_left = None
        self.tree_right = None

    def node_type(self):
        return 2

    def has_child(self):
        return self.tree_left is not None or self.tree_right is not None

    def traverse(self, key):
        if not self.has_child():
            raise "Trying to traverse a leaf node: {}".format(self)
        print("Traversing Node: {}".format(self))
        if key < self.key:
            print("To Left: {}".format(self.tree_left))
            return (-1, True)
        if key == self.key:
            print("Found: {}".format(self))
            return (0, False)
        if key > self.key:
            print("To Right: {}".format(self.tree_right))
            return (1, True)

    def make_three_tree(self, key):
        if key < self.key:
            three_node = ThreeNode(key, self.key)
        elif key > self.key:
            three_node = ThreeNode(self.key, key)
        return three_node

    def __repr__(self):
        str_to_print = "L:{}".format(self.key)
        if self.tree_left is not None:
            str_to_print = "{} :: LT: {}".format(str_to_print, self.tree_left)
        if self.tree_right is not None:
            str_to_print = "{} :: RT: {}".format(str_to_print, self.tree_right)
        return str_to_print


class ThreeNode:
    def __init__(self, key1, key2):
        self.parent = None
        self.key_left = key1
        self.key_right = key2
        self.tree_left = None
        self.tree_mid = None
        self.tree_right = None

    def node_type(self):
        return 3

    def has_child(self):
        return self.tree_left is not None or self.tree_mid is not None or self.tree_right is not None

    def traverse(self, key):
        if not self.has_child():
            raise "Trying to traverse a leaf node: {}".format(self)
        print("Traversing...")
        if key < self.key_left:
            print("To Left: {}".format(self.tree_left))
            return (-1, True)
        if key == self.key_left:
            print("Found: {}".format(self))
            return (0, False)
        if key > self.key_left:
            if key < self.key_right:
                print("To Mid: {}".format(self.tree_mid))
                return (0, True)
            if key == self.key_right:
                print("Found: {}".format(self))
                return (self, False)
            if key > self.key_right:
                print("To Right: {}".format(self.tree_mid))
                return (1, True)

    def split_node(self, key):
        if not self.has_child():
            print("Splitting leaf node")
            if key < self.key_left:
                return (TwoNode(key), self.key_left, TwoNode(self.key_right))
            elif key > self.key_left and key < self.key_right:
                return (TwoNode(self.key_left), key, TwoNode(self.key_right))
            elif key > self.key_right:
                return (TwoNode(self.key_left), self.key_right, TwoNode(key))

    def __repr__(self):
        str_to_print = "(L:{} R:{})".format(self.key_left, self.key_right)
        if self.tree_left is not None:
            str_to_print = "{} :: LT: {}".format(str_to_print, self.tree_left)
        if self.tree_mid is not None:
            str_to_print = "{} :: MT: {}".format(str_to_print, self.tree_mid)
        if self.tree_right is not None:
            str_to_print = "{} :: RT: {}".format(str_to_print, self.tree_right)
        return str_to_print
