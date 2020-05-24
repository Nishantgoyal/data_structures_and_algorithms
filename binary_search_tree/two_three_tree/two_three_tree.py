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
        if self.root is None:
            self.root = TwoNode(key)
        else:
            self.root.insert_key(key)
