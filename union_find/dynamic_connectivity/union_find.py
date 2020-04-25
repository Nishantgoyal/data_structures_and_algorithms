class UnionFind:
    '''

        Implements data structure Union Find

    '''

    def __init__(self, N):
        self._N = N
        self._components = [{i} for i in range(self._N)]

    def union(self, a, b):
        '''
            It connects set containing element `a` to set containing element `b`
        '''
        c1 = {}
        c2 = {}
        for c in self._components:
            if a in c:
                c1 = c
            if b in c:
                c2 = c
        c3 = c1.union(c2)
        if c1 in self._components:
            self._components.remove(c1)
        if c2 in self._components:
            self._components.remove(c2)
        self._components.append(c3)

    def connected(self, a, b):
        '''
            It checks if element `a` is connected to element `b`
        '''
        connected = False
        for c in self._components:
            if a in c and b in c:
                connected = True
        return connected

    def print(self):
        print("Connected Components : {}".format(self._components))
