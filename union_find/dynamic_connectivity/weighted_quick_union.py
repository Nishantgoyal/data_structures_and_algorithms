class UnionFind:
    '''

        Implements data structure Union Find using Weighted Quick Union

    '''

    def __init__(self, N):
        self._N = N
        self._components = [i for i in range(self._N)]
        self._size = [0 for _ in range(self._N)]

    def _get_root(self, ele):
        while ele != self._components[ele]:
            ele = self._components[ele]
        return ele

    def union(self, a, b):
        '''
            It connects set containing element `a` to set containing element `b`
        '''
        root_a = self._get_root(a)
        root_b = self._get_root(b)
        if root_a == root_b:
            return
        elif self._size[root_b] <= self._size[root_a]:
            self._components[root_b] = root_a
            self._size[root_a] += self._size[root_b]
        elif self._size[root_a] < self._size[root_b]:
            self._components[root_a] = root_b
            self._size[root_b] += self._size[root_a]

    def connected(self, a, b):
        '''
            It checks if element `a` is connected to element `b`
        '''
        return self._get_root(a) == self._get_root(b)

    def print(self):
        print("Connected Components   : {}".format(self._components))
        print("Size Array             : {}".format(self._size))
