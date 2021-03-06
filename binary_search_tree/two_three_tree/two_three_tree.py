from node import TwoNode, ThreeNode
import json


class TwoThreeTree:

    def __init__(self):
        self.root = None

    def print_tree(self):
        tree = self.get_tree()
        print(tree)

    def get_tree(self):
        tree = []
        if self.root is not None:
            tree = self.root.get_tree()
            fN = "{}.json".format(__file__.split(".")[0])
            with open(fN, "w") as f_out:
                json.dump(tree, f_out)
        tree = json.dumps(tree, indent=2)
        return tree

    def dump_json(self, data):
        fn = "{}_data.json".format(__name__.split(".")[0])
        with open(fn, "w") as f:
            json.dump(data, f, indent=4)

    def insert(self, key):
        print("Inserting {} into the Two Three Tree...".format(key))
        if self.root is None:
            print("Root Node is empty. Inserting into Root...")
            self.root = TwoNode(key)
        else:
            print("Tree before Insert:")
            self.root.print_tree()
            chain = []
            parent = None
            node = self.root
            while not node.is_leaf():
                print("Traversing Node: {}".format(node))
                parent = node
                chain.append(node)
                if node.type_of_node() == "TwoNode":
                    if key < node.key:
                        node = node.trees["left"]
                        if node is None:
                            node.trees["left"] = TwoNode(key)
                            return
                    elif key > node.key:
                        node = node.trees["right"]
                        if node is None:
                            node.trees["right"] = TwoNode(key)
                            return
                    else:
                        return
                else:
                    if key < node.l_key:
                        node = node.trees["left"]
                        if node is None:
                            node.trees["left"] = TwoNode(key)
                            return
                    elif node.l_key < key < node.r_key:
                        node = node.trees["mid"]
                        if node is None:
                            node.trees["mid"] = TwoNode(key)
                            return
                    elif key > node.r_key:
                        node = node.trees["right"]
                        if node is None:
                            node.trees["right"] = TwoNode(key)
                            return
                    else:
                        return
            print("Inserting into Node: {}".format(node))
            new_node = node.insert_key(key)
            if new_node is None:
                return
            if parent is None:
                self.root = new_node
                # return
            else:
                parent.replace_node(node, new_node)
            print("Tree after Insert:")
            chain.append(new_node)
            self.dilute_chain(chain)
            data = self.root.print_tree()
            # self.dump_json(data)

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
