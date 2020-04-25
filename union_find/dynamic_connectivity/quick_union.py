class UnionFind:
    '''

        Implements data structure Union Find using Quick Find

    '''

    def __init__(self, N):
        self._N = N
        self._components = [i for i in range(self._N)]

    def _get_root(self, ele):
        while ele != self._components[ele]:
            ele = self._components[ele]
        return ele

    def union(self, a, b):
        '''
            It connects set containing element `a` to set containing element `b`
        '''
        if a >= self._N or b >= self._N:
            return
        root_a = self._get_root(a)
        root_b = self._get_root(b)
        self._components[root_a] = root_b

    def connected(self, a, b):
        '''
            It checks if element `a` is connected to element `b`
        '''
        return self._get_root(a) == self._get_root(b)

    def components(self):
        return self._components
