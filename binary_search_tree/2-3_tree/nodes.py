import json
from random import randint, seed


class TwoNode:
    def __init__(self, key, parent=None):
        print("Creating a Two Node with key: {}".format(key))
        self.parent = parent
        self.key = key
        self.tree_left = None
        self.tree_right = None

    def node_type(self):
        return 2

    def has_child(self):
        return self.tree_left is not None or self.tree_right is not None

    def add_left_child(self, node):
        print("Adding Left Child: {} to Node: {}".format(node, self))
        self.tree_left = node
        node.parent = self

    def add_right_child(self, node):
        print("Adding Right Child: {} to Node: {}".format(node, self))
        self.tree_right = node
        node.parent = self

    def replace_child(self, node, new_node):
        print("Replacing Node: {} with {}".format(node, new_node))
        if node is self.tree_left:
            self.add_left_child(new_node)
        elif node is self.tree_right:
            self.add_right_child(new_node)

    def traverse(self, key):
        if not self.has_child():
            raise "Trying to traverse a leaf node: {}".format(self)
        print("Traversing a two node: {}...".format(self))
        if key < self.key:
            print("To Left: {}".format(self.tree_left))
            return (-1, True)
        if key == self.key:
            print("Found: {}".format(self))
            return (0, False)
        if key > self.key:
            print("To Right: {}".format(self.tree_right))
            return (1, True)

    def make_three_node(self, key):
        if key < self.key:
            three_node = ThreeNode(key, self.key)
        elif key > self.key:
            three_node = ThreeNode(self.key, key)
        # if self.tree_left:
        #     if self.tree_left.node_type == 2:
        #         child_key = self.tree_left.key
        #         if child_key < three_node.key_left:
        #             three_node.tree_left = self.tree_left
        #         else:
        #             three_node.add_to_mid_tree(self.tree_left)
        # if self.tree_right:
        #     if self.tree_right.node_type == 2:
        #         child_key = self.tree_right.key
        #         if child_key > three_node.key_right:
        #             three_node.tree_right = self.tree_right
        #         else:
        #             three_node.add_to_mid_tree(self.tree_right)
        return three_node

    def insert_key(self, key):
        print("Inserting key into a two node: {}".format(self))
        return self.make_three_node(key)

    def __repr__(self):
        str_to_print = "(L:{})".format(self.key)
        if self.tree_left is not None:
            str_to_print = "{} :: LT: {}".format(str_to_print, self.tree_left)
        if self.tree_right is not None:
            str_to_print = "{} :: RT: {}".format(str_to_print, self.tree_right)
        return str_to_print


class ThreeNode:
    def __init__(self, key1, key2, parent=None):
        self.parent = parent
        self.key_left = key1
        self.key_right = key2
        self.tree_left = None
        self.tree_mid = None
        self.tree_right = None

    def node_type(self):
        return 3

    def has_child(self):
        return self.tree_left is not None or self.tree_mid is not None or self.tree_right is not None

    def add_left_child(self, node):
        print("Adding Left Child: {} to Node: {}".format(node, self))
        self.tree_left = node
        node.parent = self

    def add_right_child(self, node):
        print("Adding Right Child: {} to Node: {}".format(node, self))
        self.tree_right = node
        node.parent = self

    def add_mid_child(self, node):
        print("Adding Mid Child: {} to Node: {}".format(node, self))
        self.tree_mid = node
        node.parent = self

    def replace_child(self, node, new_node):
        print("Replacing Node: {} with {}".format(node, new_node))
        if node is self.tree_left:
            self.add_left_child(new_node)
        elif node is self.tree_mid:
            self.add_mid_child(new_node)
        elif node is self.tree_right:
            self.add_right_child(new_node)

    def traverse(self, key):
        if not self.has_child():
            raise "Trying to traverse a leaf node: {}".format(self)
        print("Traversing a three node: {}...".format(self))
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
                return (0, False)
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

    def insert_key(self, key):
        pass

    def __repr__(self):
        str_to_print = "(L:{} R:{})".format(self.key_left, self.key_right)
        if self.tree_left is not None:
            str_to_print = "{} :: LT: {}".format(str_to_print, self.tree_left)
        if self.tree_mid is not None:
            str_to_print = "{} :: MT: {}".format(str_to_print, self.tree_mid)
        if self.tree_right is not None:
            str_to_print = "{} :: RT: {}".format(str_to_print, self.tree_right)
        return str_to_print
