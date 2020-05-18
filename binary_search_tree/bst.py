import json
from random import randint, seed


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.seperator = "  "
        self.tab_size = 0
        self._print("BST - Init Method")

    def insert(self, key, value):
        self._increment()
        self._print("BST - Inserting key, Value: {}".format((key, value)))
        node = self.root
        parent = None
        is_left_child = True
        while node is not None:
            key_at_node = node.key
            parent = node
            if key == key_at_node:
                self._increment()
                self._print("Key is present in the tree, updating from earlier: {} to {}...".format(
                    (node.key, node.value), (node.key, value)))
                node.value = value
                self._decrement()
                self._decrement()
                return
            elif key < key_at_node:
                self._increment()
                self._print("Key: {} is less then key: {}. Traversing Left".format(
                    key, key_at_node))
                node = node.left
                is_left_child = True
                self._decrement()
            else:
                self._increment()
                self._print("Key: {} is greater then key: {}. Traversing Right".format(
                    key, key_at_node))
                is_left_child = False
                node = node.right
                self._decrement()
        node = Node(key, value)
        if parent is None:
            self._increment()
            self._print("Inserting at root: {}".format((key, value)))
            self.root = node
            self._decrement()
        elif is_left_child:
            self._increment()
            self._print("Inserting at left: {} of parent: {}".format(
                (key, value), parent.key))
            parent.left = node
            self._decrement()
        else:
            self._increment()
            self._print("Inserting at right: {} of parent: {}".format(
                (key, value), parent.key))
            parent.right = node
            self._decrement()
        self._decrement()

    def get(self, key):
        self._increment()
        self._print("Looking for value of key: {}".format(key))
        node = self.root
        value = None
        while node is not None:
            self._increment()
            self._print(str(node.key))
            if key == node.key:
                value = node.value
                self._decrement()
                break
            if key < node.key:
                self._print("Left...")
                node = node.left
                self._decrement()
                continue
            if key > node.key:
                self._print("Right...")
                node = node.right
            self._decrement()
        self._decrement()
        if value is not None:
            self._print("Value for key: {} is {}".format(key, value))
        else:
            self._print(
                "Value for key: {} is not present in subtree".format(key))

    def delete(self, key):
        self._increment()
        self._print("Deleting key: {}".format(key))
        node = self.root
        while node != None:
            node_key = node.key
            if key == node_key:
                self._print(
                    "key {} is equal to node key: {}".format(key, node_key))
                pass
            elif key < node_key:
                self._print(
                    "key {} is less to node key: {}".format(key, node_key))
                self._print("Moving to left subtree...")
            else:
                self._print(
                    "key {} is greater to node key: {}".format(key, node_key))
                self._print("Moving to right subtree...")
                pass
            break
        self._decrement()

    def _print(self, message):
        seperator = self.seperator * self.tab_size
        message = seperator + message
        print(message)

    def _increment(self):
        self.tab_size += 1

    def _decrement(self):
        self.tab_size -= 1

    def print_tree(self):
        node = self.root
        my_tree = {}
        space = 0
        self.print_node(node, my_tree, space)
        fn = "{}_tree.json".format(__file__.split(".")[0])
        with open(fn, "w") as f:
            json.dump(my_tree, f, indent=2)

    def print_node(self, node, my_tree, space):
        if node is None:
            return
        my_tree["key"] = node.key
        my_tree["value"] = node.value
        if node.left is not None:
            my_tree["L"] = {}
            self.print_node(node.left, my_tree["L"], space)
        if node.right is not None:
            my_tree["R"] = {}
            self.print_node(node.right, my_tree["R"], space)


if __name__ == "__main__":
    bst = BST()

    seed(20)
    ele_count = 100
    req_size = 31
    while ele_count > 0:
        ele_count -= 1
        ele = randint(0, 100)
        val = chr(ord("a") + randint(0, 25))
        bst.insert(ele, val)
    bst.print_tree()

    bst.get(22)
    bst.get(9)
    # print(val)

    bst.delete(5)
