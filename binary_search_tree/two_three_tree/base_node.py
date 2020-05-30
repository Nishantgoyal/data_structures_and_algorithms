class Node:
    def __init__(self):
        self.trees = {}

    def type_of_node(self):
        return str(self.__class__).split(".")[1].split("'")[0]

    def is_leaf(self):
        return [ele for ele in self.get_children() if ele is not None] == []

    def add_child(self, child):
        if child is None:
            return
        print("Adding Child: {} to Node: {}".format(child, self))
        child_type = child.type_of_node()
        if child_type == "TwoNode":
            self.add_two_node_as_child(child)
        elif child_type == "ThreeNode":
            self.add_three_node_as_child(child)
        else:
            raise "Unable to add child of type: {}".format(child_type)

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
        for key in self.trees:
            if self.trees[key] is not None:
                if self.trees[key] == node:
                    self.trees[key] = new_node
                    return

    def get_children_json(self, json):
        for key in self.trees:
            if self.trees[key] is not None:
                json[key] = {}
                json[key]["node"] = self.trees[key]
                self.trees[key].get_children_json(json[key])
