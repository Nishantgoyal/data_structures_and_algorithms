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
            self.root = self.root.insert_key(key)
