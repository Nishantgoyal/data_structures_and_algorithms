

class TwoNode:
    '''
        APIs
         - repr
    '''

    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.tree_left = None
        self.tree_right = None

    def __repr__(self):
        return "({})".format(self.key)


class ThreeNode:
    '''
        APIs
    '''

    def __init__(self, l_key, r_key, parent):
        self.l_key = l_key
        self.r_key = r_key
        self.parent = parent
        self.tree_left = None
        self.tree_mid = None
        self.tree_right = None

    def __repr__(self):
        return "({},{})".format(self.l_key, self.r_key)
