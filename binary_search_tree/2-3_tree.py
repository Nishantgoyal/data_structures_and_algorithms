import json
from random import randint, seed


class Node:
    def __init__(self, key):

        self.key_left = key
        self.key_right = None

        self.tree_left = None
        self.tree_mid = None
        self.tree_right = None

    def is_3_tree(self):
        return self.key_right is not None

    def has_child(self):
        return self.tree_left is not None or self.tree_mid is not None or self.tree_right is not None

    def make_3_tree(self, key):
        print("Making 3 tree from: {} with key:{} ".format(str(self), key))
        if key < self.key_left:
            self.key_right = self.key_left
            self.key_left = key
        else:
            self.key_right = key
        print("Final 3 tree is: {}".format(str(self)))

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
        parent = None
        node = self.root
        while node is not None:
            print(node)
            if node.is_3_tree():
                # 3 - Tree
                print("3-tree")
                node_key_left = node.key_left
                node_key_right = node.key_right
            else:
                # 2 - Tree
                print("2-tree")
                node_key_left = node.key_left
                if not node.has_child():
                    print("Empty tree")
                    node.make_3_tree(key)
                    return
                else:
                    print("Traversing tree")
                    if key < node.key_left:
                        node = node.tree_left
                    elif key > node.key_left:
                        node = node.tree_right
                    break

        if parent is None:
            self.root = Node(key)
        # self.dump_tree()

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
