from node import TwoNode, ThreeNode


class TwoThreeTree:
    '''
        APIs:
            - __init__
            - print_tree
    '''

    def __init__(self):
        self.root = None

    def print_tree(self):
        if self.root is None:
            print("[]")
        else:
            self.root.print_tree()

    def insert(self, key):
        print("Inserting into the Two Three Tree...")
        if self.root is None:
            print("Root Node is empty. Inserting into Root...")
            self.root = TwoNode(key)
        else:
            print("Tree before Insert:")
            self.root.print_tree()
            # self.root = self.root.insert_key(key)
            parent = None
            node = self.root
            while not node.is_leaf():
                parent = node
                if node.type_of_node() == "TwoNode":
                    if key < node.key:
                        node = node.tree_left
                        if node is None:
                            node.tree_left = TwoNode(key)
                            return
                    elif key > node.key:
                        node = node.tree_right
                        if node is None:
                            node.tree_right = TwoNode(key)
                            return
                else:
                    if key < node.l_key:
                        node = node.tree_left
                        if node is None:
                            node.tree_left = TwoNode(key)
                            return
                    elif node.l_key < key < node.r_key:
                        node = node.tree_mid
                        if node is None:
                            node.tree_mid = TwoNode(key)
                            return
                    elif key > node.r_key:
                        node = node.tree_right
                        if node is None:
                            node.tree_right = TwoNode(key)
                            return
            new_node = node.insert_key(key)
            if parent is None:
                self.root = new_node
            else:
                if node == parent.tree_left:
                    parent.tree_left = new_node
                elif node == parent.tree_right:
                    parent.tree_right = new_node
                elif parent.type_of_node() == "ThreeNode":
                    if node == parent.tree_mid:
                        parent.tree_mid = new_node
            # self.root.insert_key(key)
