class Node:
    def type_of_node(self):
        return str(self.__class__).split(".")[1].split("'")[0]

    def is_leaf(self):
        return [ele for ele in self.get_children() if ele is not None] == []

    def add_child(self, child):
        if child is None:
            return
        print("Adding Child: {} to Node: {}".format(child, self))
        if child.type_of_node() == "TwoNode":
            self.add_two_node_as_child(child)
        else:
            self.add_three_node_as_child(child)

    def print_tree(self):
        tree = {}
        tree["node"] = str(self)
        self.get_children_json(tree)
        print(tree)
        return tree

    def add_child_to_node(self, node):
        children = self.get_children()
        print("Node: {} has children: {}".format(self, children))
        for child in children:
            if child:
                print("Appending child: {} of type: {} to Node: {}".format(
                    child, child.type_of_node(), node))
                node.add_child(child)

    def replace_node(self, node, new_node):
        if node == self.tree_left:
            self.tree_left = new_node
        elif node == self.tree_right:
            self.tree_right = new_node
        elif self.type_of_node() == "ThreeNode":
            if node == self.tree_mid:
                self.tree_mid = new_node


class TwoNode(Node):

    def __init__(self, key, parent=None):
        self.key = key
        self.tree_left = None
        self.tree_right = None

    def __repr__(self):
        return "({})".format(self.key)

    def get_children(self):
        return [self.tree_left, self.tree_right]

    def add_two_node_as_child(self, node):
        node_key = node.key
        if node_key < self.key:
            self.tree_left = node
        elif node_key > self.key:
            self.tree_right = node

    def add_three_node_as_child(self, node):
        if node.r_key < self.key:
            self.tree_left = node
        elif node.l_key < self.key < node.r_key:
            node_1, _, node_2 = node.split_node()
            self.tree_right = node_1
            self.tree_left = node_2
        elif self.key < node.l_key:
            self.tree_right = node

    def get_children_json(self, json):
        if self.tree_left:
            json["L"] = {}
            json["L"]["node"] = str(self.tree_left)
            self.tree_left.get_children_json(json["L"])
        if self.tree_right:
            json["R"] = {}
            json["R"]["node"] = str(self.tree_right)
            self.tree_right.get_children_json(json["R"])

    def promote(self, key):
        print("Converting node: {} into three node with key: {}".format(self, key))
        if key < self.key:
            three_node = ThreeNode(key, self.key)
        elif self.key < key:
            three_node = ThreeNode(self.key, key)
        else:
            raise "Key already present in the node"
        return three_node

    def key_in_node(self, key):
        if key == self.key:
            return True
        return False

    def insert_key(self, key):
        print("Inserting key: {} in Two-Node: {}".format(key, self))
        if self.key_in_node(key):
            return
        node = self.promote(key)
        self.add_child_to_node(node)
        return node


class ThreeNode(Node):

    def __init__(self, l_key, r_key, parent=None):
        self.l_key = l_key
        self.r_key = r_key
        self.tree_left = None
        self.tree_mid = None
        self.tree_right = None

    def __repr__(self):
        return "({},{})".format(self.l_key, self.r_key)

    def get_children(self):
        return [self.tree_left, self.tree_mid, self.tree_right]

    def add_two_node_as_child(self, node):
        if node.key < self.l_key:
            self.tree_left = node
        elif self.l_key < node.key < self.r_key:
            self.tree_mid = node
        elif self.r_key < node.key:
            self.tree_right = node

    def split_node(self):
        print("Splitting the node: {}".format(self))
        l_node = TwoNode(self.l_key)
        l_node.add_child(self.tree_left)
        l_node.add_child(self.tree_mid)

        r_node = TwoNode(self.r_key)
        r_node.add_child(self.tree_right)

        return l_node, r_node

    def add_three_node_as_child(self, node):
        node_l_key = node.l_key
        node_r_key = node.r_key
        node_l, _, node_r = node.split_node()
        if self.r_key < node_l_key:
            self.tree_right = node
        elif self.l_key < node_l_key < self.r_key < node_r_key:
            self.tree_mid = node_l
            self.tree_right = node_r
        elif self.l_key < node_r_key < self.r_key:
            self.tree_mid = node
        elif node_l_key < self.l_key and self.r_key < node_r_key:
            self.tree_left = node_l
            self.tree_right = node_r
        elif node_l_key < self.l_key < node_r_key < self.r_key:
            self.tree_left = node_l
            self.tree_mid = node_r
        elif node_l_key < self.l_key:
            self.tree_left = node

    def get_children_json(self, json):
        if self.tree_left:
            json["L"] = {}
            json["L"]["node"] = str(self.tree_left)
            self.tree_left.get_children_json(json["L"])
        if self.tree_mid:
            json["M"] = {}
            json["M"]["node"] = str(self.tree_mid)
            self.tree_mid.get_children_json(json["M"])
        if self.tree_right:
            json["R"] = {}
            json["R"]["node"] = str(self.tree_right)
            self.tree_right.get_children_json(json["R"])

    def promote(self, key):
        print("Converting Three-Node: {} with key: {} into a Temporary Four Node".format(self, key))
        if key < self.l_key:
            print("key: {} < l_key: {}".format(key, self.l_key))
            f_node = FourNode(key, self.l_key, self.r_key)
        elif self.l_key < key < self.r_key:
            print("l_key: {} < key: {} < r_key: {}".format(
                self.l_key, key, self.r_key))
            f_node = FourNode(self.l_key, key, self.r_key)
        elif self.r_key < key:
            print("r_key: {} < key: {}".format(self.r_key, key))
            f_node = FourNode(self.l_key, self.r_key, key)
        return f_node

    def key_in_node(self, key):
        if key == self.l_key:
            return True
        if key == self.r_key:
            return True
        return False

    def insert_key(self, key):
        print("Inserting key: {} in Three-Node: {}".format(key, self))
        if self.key_in_node(key):
            return None
        node = self.promote(key)
        self.add_child_to_node(node)
        return node


class FourNode(Node):

    def __init__(self, l_key, m_key, r_key):
        self.l_key = l_key
        self.m_key = m_key
        self.r_key = r_key
        self.tree_left = None
        self.tree_mid_1 = None
        self.tree_mid_2 = None
        self.tree_right = None

    def __repr__(self):
        return "({},{},{})".format(self.l_key, self.m_key, self.r_key)

    def get_children(self):
        return [self.tree_left, self.tree_mid_1, self.tree_mid_2, self.tree_right]

    def add_two_node_as_child(self, node):
        if node.key < self.l_key:
            self.tree_left = node
        elif self.l_key < node.key < self.m_key:
            self.tree_mid_1 = node
        elif self.m_key < node.key < self.r_key:
            self.tree_mid_2 = node
        elif self.r_key < node.key:
            self.tree_right = node

    def add_three_node_as_child(self, node):
        node_l, node_r = node.split_node()
        if node.l_key < node.r_key < self.l_key < self.m_key < self.r_key:
            self.tree_left = node
        elif node.l_key < self.l_key < node.r_key < self.m_key < self.r_key:
            self.tree_left = node_l
            self.tree_mid_1 = node_r
        elif node.l_key < self.l_key < self.m_key < node.r_key < self.r_key:
            self.tree_left = node_l
            self.tree_mid_2 = node_r
        elif node.l_key < self.l_key < self.m_key < self.r_key < node.r_key:
            self.tree_left = node_l
            self.tree_right = node_r
        elif self.l_key < node.l_key < node.r_key < self.m_key < self.r_key:
            self.tree_mid_1 = node
        elif self.l_key < node.l_key < self.m_key < node.r_key < self.r_key:
            self.tree_mid_1 = node_l
            self.tree_mid_2 = node_r
        elif self.l_key < node.l_key < self.m_key < self.r_key < node.r_key:
            self.tree_mid_1 = node_l
            self.tree_right = node_r
        elif self.l_key < self.m_key < node.l_key < node.r_key < self.r_key:
            self.tree_mid_2 = node
        elif self.l_key < self.m_key < node.l_key < self.r_key < node.r_key:
            self.tree_mid_2 = node_l
            self.tree_right = node_r
        elif self.l_key < self.m_key < self.r_key < node.l_key < node.r_key:
            self.tree_right = node

    def get_children_json(self, json):
        if self.tree_left:
            json["L"] = {}
            json["L"]["node"] = self.tree_left
            self.tree_left.get_children_json(json["L"])
        if self.tree_right:
            json["R"] = {}
            json["R"]["node"] = self.tree_right
            self.tree_right.get_children_json(json["R"])
        if self.tree_mid_1:
            json["M_1"] = {}
            json["M_1"]["node"] = self.tree_mid_1
            self.tree_mid_1.get_children_json(json["M_1"])

        if self.tree_mid_2:
            json["M_2"] = {}
            json["M_2"]["node"] = self.tree_mid_2
            self.tree_mid_2.get_children_json(json["M_2"])

    def split_node(self):
        print("Splitting the node: {}".format(self))
        l_node = TwoNode(self.l_key)
        l_node.add_child(self.tree_left)
        l_node.add_child(self.tree_mid_1)

        r_node = TwoNode(self.r_key)
        r_node.add_child(self.tree_mid_2)
        r_node.add_child(self.tree_right)

        return l_node, self.m_key, r_node
