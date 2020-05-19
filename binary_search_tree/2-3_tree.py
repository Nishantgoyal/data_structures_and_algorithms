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
            mid = self.key_left
            node2 = Node(self.key_right)
        elif key > self.key_left and key < self.key_right:
            node1 = Node(self.key_left)
            mid = key
            node2 = Node(self.key_right)
        elif key > self.key_right:
            node1 = Node(self.key_left)
            mid = self.key_right
            node2 = Node(key)
        return (node1, mid, node2)

    def __repr__(self):
        if self.key_right:
            return "({}-{})".format(self.key_left, self.key_right)
        else:
            return "({})".format(self.key_left)


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        print("Inserting key: {}".format(key))
        node = self.root
        print(node)
        if node.has_child():
            (node, traverse) = node.traverse()
            if traverse is False:
                print("Key already present")
                return
        else:
            pass
        # if node.is_3_tree():
        #     # 3 - Tree
        #     print("3-tree")
        #     node_key_left = node.key_left
        #     node_key_right = node.key_right
        #     if not node.has_child():
        #         print("Empty 3 tree")
        #         while parent is not None:
        #             (node1, mid, node2) = node.split_node(key)
        #             if parent.is_2_tree():
        #                 parent.make_3_tree(key)
        #             # else:
        #     else:
        #         print("Traversing tree")
        #         if key < node.key_left:
        #             node = node.tree_left
        #         elif key > node.key_left and key < node.key_right:
        #             node = node.tree_mid
        #         elif key > node.key_right:
        #             node = node.tree_right
        # else:
        #     # 2 - Tree
        #     print("2-tree")
        #     node_key_left = node.key_left
        #     if not node.has_child():
        #         print("Empty tree")
        #         node.make_3_tree(key)
        #         return
        #     else:
        #         print("Traversing tree")
        #         if key < node.key_left:
        #             node = node.tree_left
        #         elif key > node.key_left:
        #             node = node.tree_right

        # if parent is None:
        #     self.root = Node(key)
        # # self.dump_tree()

    def dump_tree(self):
        with open("{}_tree.json".format(__file__.split(".")[0]), "w") as fn:
            json_list = {}
            self.print_tree(self.root, json_list)
            json.dump(json_list, fn, indent=4)

    def print_tree(self, node, json_list):

        json_list["node"] = str(node)
        # json_list["value"] = str(node.value)
        if node.tree_left:
            json_list["left"] = {}
            node.print_tree(node.tree_left, json_list["left"])
        if node.tree_mid:
            json_list["mid"] = {}
            node.print_tree(node.tree_mid, json_list["mid"])
        if node.tree_right:
            json_list["right"] = {}
            node.print_tree(node.tree_right, json_list["right"])


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
