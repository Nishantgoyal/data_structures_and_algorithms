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
         - add_three_node_as_child
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

    def add_three_node_as_child(self, node):
        '''
            Cases:
             1. key < node_l_key < node_r_key
                Add node in right
             2. node_l_key < node_r_key < key
                Add node in left
             3. node_l_key < key < node_r_key
                split node
        '''
        if self.key < node.l_key:
            self.tree_right = node
            return
        if self.key > node.r_key:
            self.tree_left = node
            return
        node_1, _, node_2 = node.split_node()
        self.add_two_node_as_child(node_1)
        self.add_two_node_as_child(node_2)


class ThreeNode(Node):
    '''
        APIs
         - repr
         - get_children
         - add_two_node_as_child
         - split_node
         - add_three_node_as_child
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

    def split_node(self):
        l_node = TwoNode(self.l_key)
        r_node = TwoNode(self.r_key)
        l_node.tree_left = self.tree_left
        l_node.tree_right = self.tree_mid
        r_node.tree_right = self.tree_right
        return l_node, None, r_node

    def add_three_node_as_child(self, node):
        '''
            keys: 
                - l_key < r_key
                - node_l_key < node_r_key
            Cases:
              - r_key < node_l_key
                - add as right child
              - l_key < node_l_key < r_key < node_r_key
                - split node
                - add l_node as mid child
                - add r_node as right child
              - l_key < node_l_key < node_r_key < r_key
                - add node as mid child
              - node_l_key < l_key < r_key < node_r_key
                - split node
                - add l_node as left child
                - add r_node as right child
              - node_l_key < l_key < node_r_key < r_key
                - split node
                - add l_node as left child
                - add r_node as mid child
              - node_r_key < l_key
                - add node as left child
        '''
        # if self.key < node.l_key:
        #     self.tree_right = node
        #     return
        # if self.key > node.r_key:
        #     self.tree_left = node
        #     return
        # node_1, _, node_2 = node.split_node()
        # self.add_two_node_as_child(node_1)
        # self.add_two_node_as_child(node_2)


if __name__ == "__main__":
    # tn = ThreeNode(2, 3)
    tn = TwoNode(12)
    # print(tn.is_leaf())
    t1 = TwoNode(3)
    t2 = ThreeNode(1, 2)

    tn.add_three_node_as_child(t2)

    print(tn)
    print(tn.get_children())
