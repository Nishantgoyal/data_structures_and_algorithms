from base_node import Node


class TwoNode(Node):

    def __init__(self, key):
        self.key = key
        self.trees = {
            "left": None, "right": None
        }

    def __repr__(self):
        return "({})".format(self.key)

    def get_children(self):
        return [self.trees["left"], self.trees["right"]]

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

    def get_children_json(self, json):
        if self.trees["left"]:
            json["L"] = {}
            json["L"]["node"] = str(self.trees["left"])
            self.trees["left"].get_children_json(json["L"])
        if self.trees["right"]:
            json["R"] = {}
            json["R"]["node"] = str(self.trees["right"])
            self.trees["right"].get_children_json(json["R"])

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

    def __init__(self, l_key, r_key):
        self.l_key = l_key
        self.r_key = r_key
        self.trees = {
            "left": None, "mid": None, "right": None
        }

    def __repr__(self):
        return "({},{})".format(self.l_key, self.r_key)

    def get_children(self):
        return [self.trees["left"], self.trees["mid"], self.trees["right"]]

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

    def get_children_json(self, json):
        if self.trees["left"]:
            json["L"] = {}
            json["L"]["node"] = str(self.trees["left"])
            self.trees["left"].get_children_json(json["L"])
        if self.trees["mid"]:
            json["M"] = {}
            json["M"]["node"] = str(self.trees["mid"])
            self.trees["mid"].get_children_json(json["M"])
        if self.trees["right"]:
            json["R"] = {}
            json["R"]["node"] = str(self.trees["right"])
            self.trees["right"].get_children_json(json["R"])

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
        self.trees = {
            "left": None, "mid_1": None, "mid_2": None, "right": None
        }

    def __repr__(self):
        return "({},{},{})".format(self.l_key, self.m_key, self.r_key)

    def add_three_node_as_child(self, node):
        node_l, node_r = node.split_node()
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

    def get_children(self):
        return [self.trees["left"], self.trees["mid_1"], self.trees["mid_2"], self.trees["right"]]

    def get_children_json(self, json):
        if self.trees["left"]:
            json["L"] = {}
            json["L"]["node"] = self.trees["left"]
            self.trees["left"].get_children_json(json["L"])
        if self.trees["right"]:
            json["R"] = {}
            json["R"]["node"] = self.trees["right"]
            self.trees["right"].get_children_json(json["R"])
        if self.trees["mid_1"]:
            json["M_1"] = {}
            json["M_1"]["node"] = self.trees["mid_1"]
            self.trees["mid_1"].get_children_json(json["M_1"])

        if self.trees["mid_2"]:
            json["M_2"] = {}
            json["M_2"]["node"] = self.trees["mid_2"]
            self.trees["mid_2"].get_children_json(json["M_2"])

    def split_node(self):
        print("Splitting the node: {}".format(self))
        l_node = TwoNode(self.l_key)
        l_node.add_child(self.trees["left"])
        l_node.add_child(self.trees["mid_1"])

        r_node = TwoNode(self.r_key)
        r_node.add_child(self.trees["mid_2"])
        r_node.add_child(self.trees["right"])

        return l_node, self.m_key, r_node
