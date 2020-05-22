class Node:
    '''
        APIs
         - type_of_node
         - is_leaf
         - add_child
         - print_tree

        Abstract
         - add_two_node_as_child
         - add_three_node_as_child
         - get_children
         - get_children_json
         - insert_key
    '''

    def type_of_node(self):
        return str(self.__class__).split(".")[1].split("'")[0]

    def is_leaf(self):
        return self.get_children() == []

    def add_two_node_as_child(self, node):
        '''
            Abstract
        '''
        raise "Please implement method 'add_two_node_as_child'"

    def add_three_node_as_child(self, node):
        '''
            Abstract
        '''
        raise "Please implement method 'add_three_node_as_child'"

    def add_child(self, child):
        if child.type_of_node() == "TwoNode":
            self.add_two_node_as_child(child)
        else:
            self.add_three_node_as_child(child)
        child.parent = self

    def get_children(self):
        '''
            Abstract
        '''
        raise "Please implement method 'get_children'"

    def get_children_json(self, json):
        '''
            Abstract
        '''
        raise "Please implement method 'get_children_json'"

    def print_tree(self):
        tree = {}
        tree["node"] = str(self)
        self.get_children_json(tree)
        print(tree)
        return tree

    def insert_key(self, key):
        '''
            Abstract
        '''
        raise "Please implement method 'insert_key'"


class TwoNode(Node):
    '''
        APIs
         - repr
         - get_children
         - add_two_node_as_child
         - add_three_node_as_child
         - get_children_json
         - convert into three node
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
        if self.key < node.l_key:
            # key < node_l_key
            # Add node in right
            self.tree_right = node
        elif self.key > node.r_key:
            # node_r_key < key
            # Add node in left
            self.tree_left = node
        else:
            # node_l_key < key < node_r_key
            # split node
            node_1, _, node_2 = node.split_node()
            self.tree_right = node_1
            self.tree_left = node_2

    def get_children_json(self, json):
        if self.tree_left:
            json["L"] = self.tree_left
        if self.tree_right:
            json["R"] = self.tree_right

    def convert_to_three_node(self, key):
        print("Converting node: {} into three node with key: {}".format(self, key))
        children = self.get_children()
        print("Node: {} has children: {}".format(self, children))
        three_node = ThreeNode(self.key, key)
        if key < self.key:
            three_node = ThreeNode(key, self.key)
        for child in children:
            print("Appending child: {} of type: {} to Node: {}".format(
                child, child.type_of_node(), three_node))
            if child.type_of_node() == "TwoNode":
                three_node.add_two_node_as_child(child)
            else:
                three_node.add_three_node_as_child(child)
        three_node.print_tree()

    def insert_key(self, key):
        print("Inserting key: {} in Node: {}".format(key, self))
        if self.is_leaf():
            print("Node is a leaf")
        else:
            print("Node has children")


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
        node_l_key = node.l_key
        node_r_key = node.r_key
        node_l, _, node_r = node.split_node()
        if self.r_key < node_l_key:
            # Case 1: r_key < node_l_key
            # - add as right child
            self.tree_right = node

        elif self.l_key < node_l_key and node_l_key < self.r_key and self.r_key < node_r_key:
            # Case 2: l_key < node_l_key < r_key < node_r_key
            # - split node
            # - add l_node as mid child
            # - add r_node as right child
            self.tree_mid = node_l
            self.tree_right = node_r

        elif self.l_key < node_l_key and node_r_key < self.r_key:
            # Case 3: l_key < node_l_key and node_r_key < r_key
            # - add node as mid child
            self.tree_mid = node

        elif node_l_key < self.l_key and self.r_key < node_r_key:
            # Case 4: node_l_key < l_key and r_key < node_r_key
            # - split node
            # - add l_node as left child
            # - add r_node as right child
            self.tree_left = node_l
            self.tree_right = node_r

        elif node_l_key < self.l_key and self.l_key < node_r_key and node_r_key < self.r_key:
            # Case 5: node_l_key < l_key < node_r_key < r_key
            # - split node
            # - add l_node as left child
            # - add r_node as mid child
            self.tree_left = node_l
            self.tree_mid = node_r

        elif node_l_key < self.l_key:
            # Case 6: node_r_key < l_key
            # - add node as left child
            self.tree_left = node

    def get_children_json(self, json):
        if self.tree_left:
            json["L"] = self.tree_left
        if self.tree_right:
            json["R"] = self.tree_right
        if self.tree_mid:
            json["M"] = self.tree_mid

    # def insert_key(self, key):
    #     print("Inserting key: {} in Node: {}".format(key, self))


if __name__ == "__main__":
    tn = TwoNode(12)
    tn.tree_left = TwoNode(5)
    tn.tree_right = ThreeNode(15, 20)
    tn = tn.convert_to_three_node(7)
    # tn = TwoNode(12)
    # print(tn.is_leaf())
    # t1 = TwoNode(3)
    # t2 = ThreeNode(1, 20)
    # tn.insert_key(5)

    # tn.add_three_node_as_child(t2)

    # tn.print_tree()
