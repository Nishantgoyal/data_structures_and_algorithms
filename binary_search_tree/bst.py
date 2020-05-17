import json


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
        self._print("BST - Inserting Value: {}".format(value))
        node = self.root
        parent = None
        is_left_child = True
        while node is not None:
            key_at_node = node.key
            parent = node
            if key <= key_at_node:
                self._increment()
                self._print("Key: {} is less then or equal to key: {}. Traversing Left".format(
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

    def _print(self, message):
        seperator = self.seperator * self.tab_size
        message = seperator + message
        # print(message)

    def _increment(self):
        self.tab_size += 1

    def _decrement(self):
        self.tab_size -= 1

    def print_tree(self):
        node = self.root
        my_tree = {}
        space = 0
        self.print_node(node, my_tree, space)

        print(json.dumps(my_tree, indent=2))

    def print_node(self, node, my_tree, space):
        if node is None:
            return
        my_tree["ele"] = ": ".join([str(node.key), str(node.value)])
        if node.left is not None:
            my_tree["L"] = {}
            self.print_node(node.left, my_tree["L"], space)
        if node.right is not None:
            my_tree["R"] = {}
            self.print_node(node.right, my_tree["R"], space)


if __name__ == "__main__":
    bst = BST()
    bst.insert(8, "a")
    bst.insert(12, "c")
    bst.insert(10, "d")
    bst.insert(5, "s")
    bst.insert(15, "e")
    bst.print_tree()
