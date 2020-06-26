from node import Node


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def insert(self, key):
        print("\n\nInserting: {}".format(key))

        if self.root is None:
            self.root = Node(key)
            return

        is_present, chain = self.find_node_to_insert(key)

        if is_present:
            print("Key already present")
            return
        else:
            self.insert_in_tree(chain, key)

    def update(self, chain):
        if chain == []:
            return
        self.print_chain(chain)
        self.print_tree()
        node, parent = None, None
        node = chain.pop()
        is_root = False
        if len(chain) >= 1:
            parent = chain.pop()
        else:
            parent = None
            is_root = True
        new_parent, new_node = node.update(parent)
        if is_root:
            if new_parent:
                self.root = new_parent
            else:
                self.root = new_node
            return
        if new_parent is not None:
            if len(chain) >= 1:
                grandParent = chain[-1]
                parent.replace_node(grandParent, new_parent)
            else:
                self.root = new_parent
            parent = new_parent
        chain.append(parent)
        self.update(chain)

    def insert_in_tree(self, chain, key):
        print("Inserting into Tree")
        node_to_insert = Node(key, 1)
        node = chain.pop()
        node.insert(node_to_insert)
        chain.append(node)
        self.print_tree()
        self.update(chain)
        self.root.color = 0

    def find_node_to_insert(self, key):
        print("Finding Node to insert: {}".format(key))
        self.print_tree()
        is_present = False
        chain = []
        node = self.root
        while node is not None:
            chain.append(node)
            if key < node.key:
                node = node.left_child
            elif key > node.key:
                node = node.right_child
            elif key == node.key:
                is_present = True
                break
        return is_present, chain

    def print_tree(self):
        tree = {}
        if self.root is not None:
            self.root.print_node(tree)
        print(tree)

    def print_chain(self, chain):
        print("\nUpdating Chain: {}".format([str(node) for node in chain]))
