from base_node import Node


class TwoNode(Node):

    def __init__(self, key):
        self.key = key
        self.trees = {
            "left": None, "right": None
        }

    def __repr__(self):
        return "[{}]".format(self.key)

    def add_two_node_as_child(self, node):
        node_key = node.key
        if node_key < self.key:
            self.trees["left"] = node
        elif node_key > self.key:
            self.trees["right"] = node

    def add_three_node_as_child(self, node):
        if node.r_key < self.key:
            self.trees["left"] = node
        elif node.l_key < self.key < node.r_key:
            node_1, _, node_2 = node.split_node()
            self.trees["right"] = node_1
            self.trees["left"] = node_2
        elif self.key < node.l_key:
            self.trees["right"] = node

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
        if key in [self.key]:
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

    def __init__(self, l_key, r_key):
        self.l_key = l_key
        self.r_key = r_key
        self.trees = {
            "left": None, "mid": None, "right": None
        }

    def __repr__(self):
        return "[{},{}]".format(self.l_key, self.r_key)

    def add_two_node_as_child(self, node):
        if node.key < self.l_key:
            self.trees["left"] = node
        elif self.l_key < node.key < self.r_key:
            self.trees["mid"] = node
        elif self.r_key < node.key:
            self.trees["right"] = node

    def split_node(self):
        print("Splitting the node: {}".format(self))
        l_node = TwoNode(self.l_key)
        l_node.add_child(self.trees["left"])
        l_node.add_child(self.trees["mid"])

        r_node = TwoNode(self.r_key)
        r_node.add_child(self.trees["right"])

        return l_node, None, r_node

    def add_three_node_as_child(self, node):
        node_l_key = node.l_key
        node_r_key = node.r_key
        node_l, _, node_r = node.split_node()
        if self.r_key < node_l_key:
            self.trees["right"] = node
        elif self.l_key < node_l_key < self.r_key < node_r_key:
            self.trees["mid"] = node_l
            self.trees["right"] = node_r
        elif self.l_key < node_r_key < self.r_key:
            self.trees["mid"] = node
        elif node_l_key < self.l_key and self.r_key < node_r_key:
            self.trees["left"] = node_l
            self.trees["right"] = node_r
        elif node_l_key < self.l_key < node_r_key < self.r_key:
            self.trees["left"] = node_l
            self.trees["mid"] = node_r
        elif node_l_key < self.l_key:
            self.trees["left"] = node

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
        if key in [self.l_key, self.r_key]:
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
        self.trees = {
            "left": None, "mid_1": None, "mid_2": None, "right": None
        }

    def __repr__(self):
        return "[{},{},{}]".format(self.l_key, self.m_key, self.r_key)

    def add_three_node_as_child(self, node):
        node_l, _, node_r = node.split_node()
        if node.l_key < node.r_key < self.l_key < self.m_key < self.r_key:
            self.trees["left"] = node
        elif node.l_key < self.l_key < node.r_key < self.m_key < self.r_key:
            self.trees["left"] = node_l
            self.trees["mid_1"] = node_r
        elif node.l_key < self.l_key < self.m_key < node.r_key < self.r_key:
            self.trees["left"] = node_l
            self.trees["mid_2"] = node_r
        elif node.l_key < self.l_key < self.m_key < self.r_key < node.r_key:
            self.trees["left"] = node_l
            self.trees["right"] = node_r
        elif self.l_key < node.l_key < node.r_key < self.m_key < self.r_key:
            self.trees["mid_1"] = node
        elif self.l_key < node.l_key < self.m_key < node.r_key < self.r_key:
            self.trees["mid_1"] = node_l
            self.trees["mid_2"] = node_r
        elif self.l_key < node.l_key < self.m_key < self.r_key < node.r_key:
            self.trees["mid_1"] = node_l
            self.trees["right"] = node_r
        elif self.l_key < self.m_key < node.l_key < node.r_key < self.r_key:
            self.trees["mid_2"] = node
        elif self.l_key < self.m_key < node.l_key < self.r_key < node.r_key:
            self.trees["mid_2"] = node_l
            self.trees["right"] = node_r
        elif self.l_key < self.m_key < self.r_key < node.l_key < node.r_key:
            self.trees["right"] = node

    def add_two_node_as_child(self, node):
        if node.key < self.l_key:
            self.trees["left"] = node
        elif self.l_key < node.key < self.m_key:
            self.trees["mid_1"] = node
        elif self.m_key < node.key < self.r_key:
            self.trees["mid_2"] = node
        elif self.r_key < node.key:
            self.trees["right"] = node

    def split_node(self):
        print("Splitting the node: {}".format(self))
        l_node = TwoNode(self.l_key)
        l_node.add_child(self.trees["left"])
        l_node.add_child(self.trees["mid_1"])

        r_node = TwoNode(self.r_key)
        r_node.add_child(self.trees["mid_2"])
        r_node.add_child(self.trees["right"])

        return l_node, self.m_key, r_node
