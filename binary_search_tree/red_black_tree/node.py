class Node:
    def __init__(self, key, color=0):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.color = color  # Black - 0; Red - 1

    def __str__(self):
        return "Node: [{}]".format(self.key)

    def print_node(self, tree):
        tree["node"] = "{} C:{}".format(self.key, self.color)
        if self.left_child is not None:
            tree["left"] = {}
            self.left_child.print_node(tree["left"])
        if self.right_child is not None:
            tree["right"] = {}
            self.right_child.print_node(tree["right"])

    def replace_node(self, parent, node):
        print("Replacing {} with {}, Parent: {}".format(self, node, parent))
        if parent.left_child == self:
            parent.left_child = node
        else:
            parent.right_child = node

    def insert(self, node_to_insert):
        print("Inserting: {} into: {}".format(node_to_insert, self))
        node_to_insert.parent = self
        if self.key > node_to_insert.key:
            print("Inserted into Left")
            self.left_child = node_to_insert
        else:
            print("Inserted into Right")
            self.right_child = node_to_insert

    def left_rotate(self):
        print("Left Rotating: {}".format(self))
        x = self.right_child
        self.right_child = x.left_child
        x.left_child = self
        x.color, self.color = self.color, x.color
        return x

    def right_rotate(self):
        print("Right Rotating: {}".format(self))
        x = self.left_child
        self.left_child = x.right_child
        x.right_child = self
        x.color, self.color = self.color, x.color
        return x

    def toggle_color(self):
        if self.color == 0 and self.left_child.color == 1 and self.right_child.color == 1:
            print("Toggling Color of: {}".format(self))
            self.left_child.color = 0
            self.right_child.color = 0
            self.color = 1

    def update(self, parent=None):
        print("Updating {}, Parent: {}".format(self, parent))
        if self.color == 0:
            print("Node is Black")
            if self.left_child and self.left_child.color == 0:
                print("Left Child is Black")
                if self.right_child and self.right_child.color == 0:
                    print("Right Child is Black")
                    return parent, self
                elif self.right_child and self.right_child.color == 1:
                    print("Right Child is Red")
                    rotated_node = self.left_rotate()
                    print("Rotated Node: {}".format(rotated_node))
                    if parent is None:
                        return parent, rotated_node
                    self.replace_node(parent, rotated_node)
                else:
                    print("No Right Child")
                    return parent, self
            elif self.left_child and self.left_child.color == 1:
                print("Left Child is Red")
                if self.right_child and self.right_child.color == 0:
                    print("Right Child is Black")
                    return parent, self
                elif self.right_child and self.right_child.color == 1:
                    print("Right Child is Red")
                    self.toggle_color()
                    return parent, self
                else:
                    print("No Right Child")
                    return parent, self
            else:
                print("No Left Child")
                if self.right_child and self.right_child.color == 0:
                    print("Right Child is Black")
                    return parent, self
                elif self.right_child and self.right_child.color == 1:
                    print("Right Child is Red")
                    rotated_node = self.left_rotate()
                    print("Rotated Node: {}".format(rotated_node))
                    if parent is None:
                        return parent, rotated_node
                    self.replace_node(parent, rotated_node)
                    return parent, self
                else:
                    print("No Right Child")
                    return parent, self
        else:
            print("Node is Red")
            if self.left_child and self.left_child.color == 0:
                print("Left Child is Black")
                if self.right_child and self.right_child.color == 0:
                    print("Right Child is Black")
                    return parent, self
                elif self.right_child and self.right_child.color == 1:
                    print("Right Child is Red")
                    rotated_node = self.left_rotate()
                    self.replace_node(parent, rotated_node)
                    rotated_parent = parent.right_rotate()
                    print("Rotated Parent: {}".format(rotated_parent))
                    return rotated_parent, self
                else:
                    print("No Right Child")
                    return parent, self
            elif self.left_child and self.left_child.color == 1:
                print("Left Child is Red")
                if self.right_child and self.right_child.color == 0:
                    print("Right Child is Black")
                    return parent, self
                elif self.right_child and self.right_child.color == 1:
                    print("Right Child is Red")
                    self.toggle_color()
                    return parent, self
                else:
                    print("No Right Child")
                    rotated_parent = parent.right_rotate()
                    print("Rotated Parent: {}".format(rotated_parent))
                    return rotated_parent, self
            else:
                print("No Left Child")
                if self.right_child and self.right_child.color == 0:
                    print("Right Child is Black")
                    return parent, self
                elif self.right_child and self.right_child.color == 1:
                    print("Right Child is Red")
                    rotated_node = self.left_rotate()
                    self.replace_node(parent, rotated_node)
                    rotated_parent = parent.right_rotate()
                    print("Rotated Parent: {}".format(rotated_parent))
                    return rotated_parent, self
                else:
                    print("No Right Child")
                    return parent, self
