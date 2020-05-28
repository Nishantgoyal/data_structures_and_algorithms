from node import TwoNode, ThreeNode
import json


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

    def dump_json(self, data):
        fn = "{}_data.json".format(__name__.split(".")[0])
        with open(fn, "w") as f:
            json.dump(data, fn, indent=4)

    def insert(self, key):
        print("Inserting into the Two Three Tree...")
        if self.root is None:
            print("Root Node is empty. Inserting into Root...")
            self.root = TwoNode(key)
        else:
            print("Tree before Insert:")
            self.root.print_tree()
            # self.root = self.root.insert_key(key)
            chain = []
            parent = None
            node = self.root
            while not node.is_leaf():
                parent = node
                chain.append(node)
                if node.type_of_node() == "TwoNode":
                    if key < node.key:
                        node = node.tree_left
                        if node is None:
                            node.tree_left = TwoNode(key)
                            return
                    elif key > node.key:
                        node = node.tree_right
                        if node is None:
                            node.tree_right = TwoNode(key)
                            return
                else:
                    if key < node.l_key:
                        node = node.tree_left
                        if node is None:
                            node.tree_left = TwoNode(key)
                            return
                    elif node.l_key < key < node.r_key:
                        node = node.tree_mid
                        if node is None:
                            node.tree_mid = TwoNode(key)
                            return
                    elif key > node.r_key:
                        node = node.tree_right
                        if node is None:
                            node.tree_right = TwoNode(key)
                            return
            new_node = node.insert_key(key)
            if parent is None:
                self.root = new_node
                # return
            else:
                parent.replace_node(node, new_node)
            print("Tree after Insert:")
            self.root.print_tree()
            chain.append(new_node)
            self.dilute_chain(chain)
            # data = self.root.get_children_json()

    def dilute_chain(self, chain):
        print("Chain: {}".format(chain))

        node = chain.pop()
        print("Node: {}".format(node))

        if node.type_of_node() != "FourNode":
            return

        node_l, mid, node_r = node.split_node()

        if chain == []:
            self.root = TwoNode(mid)
            self.root.add_child(node_l)
            self.root.add_child(node_r)
            return

        parent = chain.pop()
        print("Parent is: {}".format(parent))
        parent.replace_node(node, None)

        new_parent = parent.promote(mid)
        print("Promoted parent: {} to: {}".format(parent, new_parent))

        parent.add_child_to_node(new_parent)
        new_parent.add_child(node_l)
        new_parent.add_child(node_r)

        if chain == []:
            self.root = new_parent
        else:
            g_parent = chain[-1]
            g_parent.replace_node(parent, new_parent)
        chain.append(new_parent)
        self.dilute_chain(chain)
