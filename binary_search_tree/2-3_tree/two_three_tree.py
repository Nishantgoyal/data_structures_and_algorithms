import json
from random import randint, seed


class TwoThreeTree:

    def __init__(self):
        self.root = None

    # def insert(self, key, node=None):
    #     print("Inserting key: {}".format(key))
    #     if self.root == None:
    #         print("Inserting root element...")
    #         self.root = Node(key)
    #     if node is None:
    #         node = self.root
    #     if node.has_child():
    #         print("Node: {} has child...".format(node))
    #         (direction, traverse) = node.traverse(key)
    #         if traverse is False:
    #             print("Key already present")
    #             return
    #         else:
    #             if direction == -1:
    #                 # Insert in left tree
    #                 if node.tree_left is not None:
    #                     self.insert(key, node.tree_left)
    #                 else:
    #                     node.tree_left = Node(key)
    #                     node.tree_left.parent = node
    #             elif direction == 0:
    #                 # Insert in mid tree
    #                 if node.tree_mid is not None:
    #                     self.insert(key, node.tree_mid)
    #                 else:
    #                     node.tree_mid = Node(key)
    #                     node.tree_mid.parent = node
    #             else:
    #                 if node.tree_right is not None:
    #                     self.insert(key, node.tree_right)
    #                 else:
    #                     node.tree_right = Node(key)
    #                     node.tree_right.parent = node
    #     else:
    #         print("Node is leaf...")
    #         parent = node.parent
    #         if parent is None:
    #             self.root = self.insert_key(key, node)
    #         else:
    #             # self.insert_key(key, node)
    #             if node is parent.tree_left:
    #                 parent.tree_left = self.insert_key(key, node)
    #             elif node is parent.tree_mid:
    #                 parent.tree_mid = self.insert_key(key, node)
    #             elif node is parent.tree_right:
    #                 parent.tree_right = self.insert_key(key, node)

    # def insert_key(self, node, key, node1=None, node2=None):
    #     print("Inserting key: {} in Node: {}".format(key, node))
    #     if node.is_3_tree():
    #         print("Node: {} is 3 tree".format(node))
    #         (node1, mid, node2) = node.split_node(key)
    #         print("Node split: {} {} {}".format(node1, mid, node2))
    #         if node.parent is None:
    #             # Create a 2-tree parent and add node 1 as left child, and node 2 as right child
    #             print("Node: {} parent is None".format(node))
    #             node = Node(mid)
    #             print("Created Node: {}".format(node))
    #             node.tree_left = node1
    #             node.tree_right = node2
    #             node1.parent = node
    #             node2.parent = node
    #             return node
    #         else:
    #             node.parent = node.parent.insert_key(key)
    #             if node.parent.tree_left:

    #             return node

    #     else:
    #         print("Node: {} is 2 tree".format(node))
    #         node.make_3_tree(key)
    #         return node

    # def dump_tree(self):
    #     with open("{}_tree.json".format(__file__.split(".")[0]), "w") as fn:
    #         json_list = {}
    #         print("Calling Print TwoThreeTree")
    #         self.print_tree(self.root, json_list)
    #         json.dump(json_list, fn, indent=4)

    # def print_tree(self, node, json_list):
    #     print(node)
    #     json_list["node"] = str(node)
    #     if node.tree_left:
    #         json_list["left"] = {}
    #         self.print_tree(node.tree_left, json_list["left"])
    #     if node.tree_mid:
    #         json_list["mid"] = {}
    #         self.print_tree(node.tree_mid, json_list["mid"])
    #     if node.tree_right:
    #         json_list["right"] = {}
    #         self.print_tree(node.tree_right, json_list["right"])
