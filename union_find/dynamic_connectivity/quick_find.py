class UnionFind:
    '''

        Implements data structure Union Find using Quick Find

    '''

    def __init__(self, N):
        self._N = N
        self._components = [i for i in range(self._N)]

    def union(self, a, b):
        '''
            It connects set containing element `a` to set containing element `b`
        '''
        if a >= self._N or b >= self._N:
            return
        group_b = self._components[b]
        group_a = self._components[a]
        for i in range(1, len(self._components) + 1):
            if self._components[i - 1] == group_a:
                self._components[i - 1] = group_b

    def connected(self, a, b):
        '''
            It checks if element `a` is connected to element `b`
        '''
        if a >= self._N or b >= self._N:
            return
        return self._components[a] == self._components[b]

    def print(self):
        print("Connected Components : {}".format(self._components))
