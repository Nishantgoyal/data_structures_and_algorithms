import json
from random import randint, seed


class Node:
    def __init__(self, key):
        self.parent = None

        self.key_left = key
        self.key_right = None

        self.tree_left = None
        self.tree_mid = None
        self.tree_right = None

    def is_3_tree(self):
        return self.key_right is not None

    def has_child(self):
        return self.tree_left is not None or self.tree_mid is not None or self.tree_right is not None

    def traverse(self, key):
        if self.key_left and key < self.key_left:
            return (self.tree_left, True)
        if self.key_left and key == self.key_left:
            return (self, False)
        if self.key_left and key > self.key_right:
            if not self.key_right:
                return (self.tree_right, True)
            else:
                if key < self.key_right:
                    return (self.tree_mid, True)
                if key == self.key_right:
                    return (self, False)
                return (self.tree_right, True)

    def make_3_tree(self, key):
        print("Making 3 tree from: {} with key:{} ".format(str(self), key))
        if key < self.key_left:
            self.key_right = self.key_left
            self.key_left = key
        elif key > self.key_left:
            self.key_right = key
        print("Final 3 tree is: {}".format(str(self)))

    def split_node(self, key):

        if key < self.key_left:
            node1 = Node(key)
            if self.tree_left is not None:
                if self.tree_left.key_left < key:
                    node1.tree_left = self.tree_left
                else:
                    node1.tree_right = self.tree_left
            mid = self.key_left
            node2 = Node(self.key_right)
            if self.tree_mid is not None:
                node2.tree_left = self.tree_mid
            if self.tree_right is not None:
                node2.tree_right = self.tree_right

        elif key > self.key_left and key < self.key_right:
            node1 = Node(self.key_left)
            if self.tree_left is not None:
                node1.tree_left = self.tree_left
            mid = key
            node2 = Node(self.key_right)
            if self.tree_mid is not None:
                if self.tree_mid.key_left < key:
                    node1.tree_right = self.tree_mid
                else:
                    node2.tree_left = self.tree_mid
            if self.tree_right is not None:
                node2.tree_right = self.tree_right

        elif key > self.key_right:
            node1 = Node(self.key_left)
            if self.tree_left is not None:
                node1.tree_left = self.tree_left
            if self.tree_mid is not None:
                node1.tree_right = self.tree_mid
            mid = self.key_right
            node2 = Node(key)
            if self.tree_right is not None:
                if self.tree_right.key_left < key:
                    node2.tree_left = self.tree_right
                else:
                    node2.tree_right = self.tree_right
        return (node1, mid, node2)

    def insert_key(self, key):
        print("Inserting key: {} in Node: {}".format(key, self))
        if self.is_3_tree():
            print("Node: {} is 3 tree".format(self))
            (node1, mid, node2) = self.split_node(key)
            print("Node split: {} {} {}".format(node1, mid, node2))
            if self.parent is None:
                print("Node: {} parent is None".format(self))
                node = Node(mid)
                print("Created Node: {}".format(node))
                node.tree_left = node1
                # print("Created Node: Left {}".format(node.tree_left))
                node.tree_right = node2
                node1.parent = node
                node2.parent = node
                return node
            else:
                self.parent = self.parent.insert_key(key)
                return self

        else:
            print("Node: {} is 2 tree")
            self.make_3_tree(key)
            return self

    def __repr__(self):
        str_to_print = "L:{}".format(self.key_left)

        if self.key_right is not None:
            str_to_print = "({} R:{})".format(str_to_print, self.key_right)
        if self.parent is not None:
            str_to_print = "P: ({}) --> {}".format(self.parent, str_to_print)
        return str_to_print


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        print("\nInserting key: {}".format(key))
        if self.root == None:
            print("Inserting root element...")
            self.root = Node(key)
        node = self.root
        if node.has_child():
            print("Node has child...")
            (node, traverse) = node.traverse(key)
            if traverse is False:
                print("Key already present")
                return
        else:
            print("Node is leaf...")
            parent = node.parent
            if parent is None:
                self.root = node.insert_key(key)
            else:
                pass

    def dump_tree(self):
        with open("{}_tree.json".format(__file__.split(".")[0]), "w") as fn:
            json_list = {}
            print("Calling Print Tree")
            self.print_tree(self.root, json_list)
            json.dump(json_list, fn, indent=4)

    def print_tree(self, node, json_list):
        print(node)
        json_list["node"] = str(node)
        if node.tree_left:
            json_list["left"] = {}
            self.print_tree(node.tree_left, json_list["left"])
        if node.tree_mid:
            json_list["mid"] = {}
            self.print_tree(node.tree_mid, json_list["mid"])
        if node.tree_right:
            json_list["right"] = {}
            self.print_tree(node.tree_right, json_list["right"])


if __name__ == "__main__":
    tree = Tree()
    tree.insert(14)
    tree.insert(4)
    tree.insert(8)
    tree.dump_tree()
    # seed(20)
    # ele_count = 1
    # while ele_count > 0:
    #     ele_count -= 1
    #     ele = randint(0, 100)
    #     val = chr(ord("a") + randint(0, 25))
    #     tree.insert(ele, val)

    # # tree.get(22)
    # # tree.get(9)
    # # # print(val)

    # tree.delete(92)
