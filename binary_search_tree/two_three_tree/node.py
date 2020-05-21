class Node:
    '''
        APIs
         - type_of_node
         - is_leaf
    '''

    def type_of_node(self):
        return str(self.__class__).split(".")[1].split("'")[0]

    def is_leaf(self):
        return self.get_children() == []

    def get_children(self):
        '''
            Abstract
        '''
        raise "Please implement method 'get_children'"


class TwoNode(Node):
    '''
        APIs
         - repr
         - get_children
         - add_two_node_as_child
    '''

    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.tree_left = None
        self.tree_right = None

    def __repr__(self):
        return "({})".format(self.key)

    def get_children(self):
        children = []
        if self.tree_left:
            children.append(self.tree_left)
        if self.tree_right:
            children.append(self.tree_right)
        return children

    def add_two_node_as_child(self, node):
        node_key = node.key
        if node_key < self.key:
            self.tree_left = node
            return
        self.tree_right = node


class ThreeNode(Node):
    '''
        APIs
         - repr
         - get_children
         - add_two_node_as_child
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

    def get_children(self):
        children = []
        if self.tree_left:
            children.append(self.tree_left)
        if self.tree_mid:
            children.append(self.tree_mid)
        if self.tree_right:
            children.append(self.tree_right)
        return children

    def add_two_node_as_child(self, node):
        node_key = node.key
        if node_key < self.l_key:
            self.tree_left = node
            return
        if node_key < self.r_key:
            self.tree_mid = node
            return
        self.tree_right = node


if __name__ == "__main__":
    tn = ThreeNode(2, 3)
    # tn = TwoNode(2)
    # print(tn.is_leaf())
    t1 = TwoNode(3)
    t2 = ThreeNode(13, 14)

    tn.add_two_node_as_child(t1)

    print(tn)
    print(tn.get_children())
