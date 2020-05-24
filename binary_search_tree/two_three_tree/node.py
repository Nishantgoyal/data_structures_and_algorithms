class Node:
    '''
        Methods
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
        if child is None:
            return
        print("Type of child: {} is {}".format(child, child.type_of_node()))
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
        Methods
         - __init__
         - __repr__
         - get_children
         - add_two_node_as_child
         - add_three_node_as_child
         - get_children_json
         - convert into three node
         - insert_key
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
            json["L"] = {}
            json["L"]["node"] = self.tree_left
            self.tree_left.get_children_json(json["L"])
        if self.tree_right:
            json["R"] = {}
            json["R"]["node"] = self.tree_right
            self.tree_right.get_children_json(json["R"])

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
            three_node.add_child(child)
        # three_node.print_tree()
        return three_node

    def insert_key(self, key):
        '''
            Inserting a Key into a 2-Node
            Case 1: Node is a leaf
                - convert to a 3-tree
            Case 2: Node has children
                Case 2.1: key is less then node_key, and left child exist
                    - Insert in left child
                Case 2.1: key is less then node_key, and left child does not exist
                    - Create 2-Node left child with key
                Case 2.1: key is greater then node_key, and right child exist
                    - Insert in right child
                Case 2.1: key is greater then node_key, and right child does not exist
                    - Create 2-Node Right Child with key
            Returns the node after insertion is complete
        '''
        print("Inserting key: {} in Two-Node: {}".format(key, self))
        if self.is_leaf():
            print("Node is a leaf")
            self = self.convert_to_three_node(key)
        else:
            print("Node has children")
            if key < self.key:
                if self.tree_left:
                    self.tree_left = self.tree_left.insert_key(key)
                else:
                    node = TwoNode(key)
                    self.add_child(node)
            elif key > self.key:
                if self.tree_right:
                    self.tree_right = self.tree_right.insert_key(key)
                else:
                    node = TwoNode(key)
                    self.add_child(node)
        return self


class ThreeNode(Node):
    '''
        Methods
         - __init__
         - __repr__
         - get_children
         - add_two_node_as_child
         - split_node
         - split_node_with_key
         - add_three_node_as_child
         - get_children_json
         - insert_key
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
        l_node.add_child(self.tree_left)
        l_node.add_child(self.tree_mid)
        r_node.add_child(self.tree_right)
        return l_node, None, r_node

    def split_node_with_key(self, key):
        '''
            Input:
                - 3-Node
                    - l_key < r_key
                    - tree_left
                    - tree_mid
                    - tree_right
                - key
            Cases:
                1 key < l_key
                    - l_node = TwoNode(key)
                    - r_node = TwoNode(r_key)
                    - mid = l_key
                    - l_node.tree_left = node.tree_left
                    - r_node.tree_left = node.tree_mid
                    - r_node.tree_right = node.tree_right
                2 l_key < key < r_key
                    - l_node = TwoNode(l_key)
                    - r_node = TwoNode(r_key)
                    - mid = key
                    - l_node.tree_left = node.tree_left
                    - r_node.tree_right = node.tree_right
                    2.1: middle child is a 3-node:
                        2.1.1: key < mc.l_key
                            - r_node.tree_left = node.tree_mid
                        2.1.2: mc.l_key < key < mc.r_key
                            - split(mc) --> mc1, mc2
                            - l_node.tree_right = mc1
                            - r_node.tree_left = mc2
                        2.1.3: mc.r_key < key
                            - l_node.tree_right = node.tree_mid
                    2.2: middle child is a 2-node:
                        2.2.1: key < mc.key
                            - r_node.tree_left = node.tree_mid
                        2.2.2: key > mc.key
                            - l_node.tree_right = node.tree_mid
                3 r_key < key
                    - l_node = TwoNode(l_key)
                    - r_node = TwoNode(key)
                    - mid = r_key
                    - l_node.tree_left = node.tree_left
                    - l_node.tree_right = node.tree_mid
                    - r_node.tree_right = node.tree_right
        '''
        print("Splitting Three-Node: {} with key: {}".format(self, key))
        if key < self.l_key:
            print("key: {} < l_key: {}".format(key, self.l_key))
            l_node = TwoNode(key)
            mid = self.l_key
            r_node = TwoNode(self.r_key)
            l_node.add_child(self.tree_left)
            r_node.add_child(self.tree_mid)
            r_node.add_child(self.tree_right)
        elif self.l_key < key < self.r_key:
            print("l_key: {} < key: {} < r_key: {}".format(
                self.l_key, key, self.r_key))
            l_node = TwoNode(self.l_key)
            mid = key
            r_node = TwoNode(self.r_key)
            l_node.add_child(self.tree_left)
            r_node.add_child(self.tree_right)
            if self.tree_mid:
                if self.tree_mid.type_of_node() == "TwoNode":
                    if key < self.tree_mid.key:
                        r_node.add_child(self.tree_mid)
                    elif key > self.tree_mid.key:
                        l_node.add_three_node_as_child(self.tree_mid)
                else:
                    if key < self.tree_mid.l_key:
                        r_node.add_child(self.tree_mid)
                    elif self.tree_mid.l_key < key < self.tree_mid.r_key:
                        mc_1, _, mc_2 = self.tree_mid.split_node()
                        l_node.add_child(mc_1)
                        r_node.add_child(mc_2)
                    elif self.tree_mid.r_key < key:
                        l_node.add_child(self.tree_mid)
        elif self.r_key < key:
            print("r_key: {} < key: {}".format(self.r_key, key))
            l_node = TwoNode(self.l_key)
            mid = self.r_key
            r_node = TwoNode(key)
            l_node.add_child(self.tree_left)
            r_node.add_child(self.tree_mid)
            r_node.add_child(self.tree_right)
        print("Three Node: {} is split into {}, {}, {}".format(
            self, l_node, mid, r_node))
        return l_node, mid, r_node

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
            json["L"] = {}
            json["L"]["node"] = self.tree_left
            self.tree_left.get_children_json(json["L"])
        if self.tree_right:
            json["R"] = {}
            json["R"]["node"] = self.tree_right
            self.tree_right.get_children_json(json["R"])
        if self.tree_mid:
            json["M"] = {}
            json["M"]["node"] = self.tree_mid
            self.tree_mid.get_children_json(json["M"])

    def insert_key(self, key):
        '''
            Inserting a key into a 3-node
            keys:
                - l_key, r_key
                - key
            Case 1: node is a leaf
                - split the three node into two two-nodes - l_node, r_node
                Case 1.1: node has no parent
                    - create a two-node with mid, and add l_node and r_node as child
                    - return mid
                Case 1.2: node has a parent
                    - parent = node.parent
                    Case 1.2.1 if parent is two_node
                        - convert parent to three node with key
                        - this will also split the child
                    Case 1.2.2 if parent is three_node
                        - split parent with key
            Case 2: node has children
                Children:
                    - l_tree
                    - m_tree
                    - r_tree
                Case 2.1: if key < l_key
                    - Case 2.1.1: l_tree exist
                        - insert the key into left tree
                    - Case 2.1.2: l_tree does not exist
                        - create a 2-Node with key
                        - insert the 2-Node in left tree
                Case 2.2: if l_key < key < r_key
                    - Case 2.2.1: m_tree exist
                        - insert the key into mid tree
                    - Case 2.2.2: m_tree does not exist
                        - create a 2-Node with key
                        - insert the 2-Node in mid tree
                Case 2.3: if r_key < key
                    - Case 2.3.1: r_tree exist
                        - insert the key into right tree
                    - Case 2.3.2: r_tree does not exist
                        - create a 2-Node with key
                        - insert the 2-Node in right tree
        '''
        print("Inserting key: {} in Three-Node: {}".format(key, self))
        if self.is_leaf():
            print("Node is a leaf")
            l_node, mid, r_node = self.split_node_with_key(key)
            print("Node: {} is split into {}, {}, {}".format(
                self, l_node, mid, r_node))
            if not self.parent:
                print("Node: {} does not have parents".format(self))
                mid_node = TwoNode(mid)
                mid_node.add_child(l_node)
                mid_node.add_child(r_node)
                return mid_node
            else:
                print("Node: {} has parents".format(self))
                if self.parent.type_of_node() == "TwoNode":
                    self.parent = self.parent.convert_to_three_node(key)
                else:
                    self.parent = self.parent.insert_key(key)
        else:
            print("Node has children")
            if key < self.l_key:
                if self.tree_left:
                    self.tree_left = self.tree_left.insert_key(key)
                else:
                    node = TwoNode(key)
                    self.add_three_node_as_child(node)
            elif self.l_key < key < self.r_key:
                if self.tree_mid:
                    self.tree_mid = self.tree_mid.insert_key(key)
                else:
                    node = TwoNode(key)
                    self.add_three_node_as_child(node)
            elif self.r_key < key:
                if self.tree_right:
                    self.tree_right = self.tree_right.insert_key(key)
                else:
                    node = TwoNode(key)
                    self.add_three_node_as_child(node)
        return self


# if __name__ == "__main__":
#     tn = TwoNode(22)
#     tn = ThreeNode(15, 20)
#     # tn.tree_left = TwoNode(5)
#     # tn.tree_right = ThreeNode(15, 20)
#     # tn = tn.convert_to_three_node(7)
#     # tn = TwoNode(12)
#     # print(tn.is_leaf())
#     # t1 = TwoNode(3)
#     # t2 = ThreeNode(1, 20)
#     tn = tn.insert_key(13)

#     # tn.add_three_node_as_child(t2)

#     tn.print_tree()
