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
        self.trace("BST - Init Method")

    def insert(self, key, value):
        self._increment()
        self.trace("BST - Inserting key, Value: {}".format((key, value)))
        node = self.root
        parent = None
        is_left_child = True
        while node is not None:
            key_at_node = node.key
            parent = node
            if key == key_at_node:
                self._increment()
                self.trace("Key is present in the tree, updating from earlier: {} to {}...".format(
                    (node.key, node.value), (node.key, value)))
                node.value = value
                self._decrement()
                self._decrement()
                return
            elif key < key_at_node:
                self._increment()
                self.trace("Key: {} is less then key: {}. Traversing Left".format(
                    key, key_at_node))
                node = node.left
                is_left_child = True
                self._decrement()
            else:
                self._increment()
                self.trace("Key: {} is greater then key: {}. Traversing Right".format(
                    key, key_at_node))
                is_left_child = False
                node = node.right
                self._decrement()
        node = Node(key, value)
        if parent is None:
            self._increment()
            self.trace("Inserting at root: {}".format((key, value)))
            self.root = node
            self._decrement()
        elif is_left_child:
            self._increment()
            self.trace("Inserting at left: {} of parent: {}".format(
                (key, value), parent.key))
            parent.left = node
            self._decrement()
        else:
            self._increment()
            self.trace("Inserting at right: {} of parent: {}".format(
                (key, value), parent.key))
            parent.right = node
            self._decrement()
        self._decrement()

    def get(self, key):
        self._increment()
        self.trace("Looking for value of key: {}".format(key))
        node = self.root
        value = None
        while node is not None:
            self._increment()
            self.trace(str(node.key))
            if key == node.key:
                value = node.value
                self._decrement()
                break
            if key < node.key:
                self.trace("Left...")
                node = node.left
                self._decrement()
                continue
            if key > node.key:
                self.trace("Right...")
                node = node.right
            self._decrement()
        self._decrement()
        if value is not None:
            self.trace("Value for key: {} is {}".format(key, value))
        else:
            self.trace(
                "Value for key: {} is not present in subtree".format(key))

    def delete(self, key):
        self._increment()
        self.trace("Deleting key: {}".format(key))
        parent = None
        node = self.root
        key_present = False
        while node != None:
            node_key = node.key
            if key == node_key:
                self.trace(
                    "key {} is equal to node key: {}".format(key, node_key))
                key_present = True
                self.delete_node(parent, node)
                break
            elif key < node_key:
                self.trace(
                    "key {} is less to node key: {}".format(key, node_key))
                self.trace("Moving to left subtree...")
                parent = node
                node = node.left
            else:
                self.trace(
                    "key {} is greater to node key: {}".format(key, node_key))
                self.trace("Moving to right subtree...")
                parent = node
                node = node.right
        if not key_present:
            self.trace("Key not present in Tree")
        self.dump_tree()
        self._decrement()

    def delete_node(self, parent, node):
        self._increment()
        if parent == None:
            self.trace("Need to delete root element")
            successor = self.get_successor(node)
            self.delete(successor.key)
            successor.left = node.left
            successor.right = node.right
            self.root = successor
            return

        self.trace("Deleting Node: {} from parent: {}".format(
            node.key, parent.key))
        is_left_child = False
        if node.key == parent.left.key:
            is_left_child = True
        self.trace("Is left Child: {}".format(is_left_child))

        # No child
        if node.left == None and node.right == None:
            self.trace("The Node has no children: {}".format(is_left_child))
            self.append_node_to_parent(parent, None, is_left_child)
            return

        # if only left child
        if node.right == None:
            self.append_node_to_parent(parent, node.left, is_left_child)
            return

        # If only right child
        if node.left == None:
            self.append_node_to_parent(parent, node.right, is_left_child)
            return

        # If both child
        # Get Successor
        successor = self.get_successor(node)
        self.delete(successor.key)
        successor.left = node.left
        successor.right = node.right
        self.append_node_to_parent(parent, successor, is_left_child)
        self._decrement()

    def append_node_to_parent(self, parent, node, is_left_child):
        if is_left_child:
            parent.left = node
        else:
            parent.right = node

    def get_successor(self, node):
        self._increment()
        right = node.right
        successor = right
        next_node = right.left
        while next_node is not None:
            successor = next_node
            next_node = next_node.left
        self._decrement()
        return successor

    def trace(self, message):
        seperator = self.seperator * self.tab_size
        message = seperator + message
        print(message)

    def _increment(self):
        self.tab_size += 1

    def _decrement(self):
        self.tab_size -= 1

    def dump_tree(self):
        node = self.root
        my_tree = {}
        space = 0
        self.get_trace_of_node(node, my_tree, space)
        fn = "{}_tree.json".format(__file__.split(".")[0])
        with open(fn, "w") as f:
            json.dump(my_tree, f, indent=2)

    def get_trace_of_node(self, node, my_tree, space):
        if node is None:
            return
        my_tree["key"] = node.key
        my_tree["value"] = node.value
        if node.left is not None:
            my_tree["L"] = {}
            self.get_trace_of_node(node.left, my_tree["L"], space)
        if node.right is not None:
            my_tree["R"] = {}
            self.get_trace_of_node(node.right, my_tree["R"], space)


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
    bst.dump_tree()

    # bst.get(22)
    # bst.get(9)
    # # print(val)

    bst.delete(92)
