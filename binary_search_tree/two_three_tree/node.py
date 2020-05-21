class Node:
    def type_of_node(self):
        return str(self.__class__).split(".")[1].split("'")[0]


class TwoNode(Node):
    '''
        APIs
         - repr
         - is_leaf
         - get_children
         - type_of_node
    '''

    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.tree_left = None
        self.tree_right = None

    def __repr__(self):
        return "({})".format(self.key)

    def is_leaf(self):
        return self.get_children() == []

    def get_children(self):
        children = []
        if self.tree_left:
            children.append(self.tree_left)
        if self.tree_right:
            children.append(self.tree_right)
        return children


class ThreeNode(Node):
    '''
        APIs
         - repr
         - is_leaf
         - get_children
         - type_of_node
    '''

    def __init__(self, l_key, r_key, parent=None):
        self.l_key = l_key
        self.r_key = r_key
        self.parent = parent
        self.tree_left = None
        self.tree_mid = None
        self.tree_right = None

    def __repr__(self):
        return "({},{})".format(self.l_key, self.r_key)

    def is_leaf(self):
        return self.get_children() == []

    def get_children(self):
        children = []
        if self.tree_left:
            children.append(self.tree_left)
        if self.tree_mid:
            children.append(self.tree_mid)
        if self.tree_right:
            children.append(self.tree_right)
        return children


if __name__ == "__main__":
    tn = TwoNode(2)
    print(tn)
    print(tn.is_leaf())
    t2 = ThreeNode(3, 2)
    tn.tree_left = t2
    print(tn.get_children())
    print(tn.type_of_node())
