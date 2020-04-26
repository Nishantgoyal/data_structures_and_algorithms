import random


class Percolate:
    def __init__(self, n):
        '''
            Input:
                n: dimension of lattice
        '''
        self._N = n
        self._start = (0, 0)
        self._lattice = [[(j, i) for i in range(n)]
                         for j in range(n)]
        self._end = (n-1, n-1)
        self.print_percolation_tree()
        self.join_start_end_nodes()
        self.print_percolation_tree()

    def join_start_end_nodes(self):
        for node in self._lattice[0][1:]:
            self.union(self._lattice[0][0], node)
        for node in self._lattice[-1][:-1]:
            self.union(self._lattice[-1][-1], node)

    def _get_root(self, ele):
        while ele != self._lattice[ele[0]][ele[1]]:
            ele = self._lattice[ele[0]][ele[1]]
        return ele

    def union(self, a, b):
        '''
            It connects set containing element `a` to set containing element `b`
        '''
        root_a = self._get_root(a)
        root_b = self._get_root(b)
        self._lattice[root_a[0]][root_a[1]] = root_b

    def print_percolation_tree(self):
        print("********" * self._N)
        print(self._start)
        for ele in self._lattice:
            print(ele)
        print(self._end)
        print("********" * self._N)

    def does_percolate(self):
        percolates = self._get_root(self._start) == self._get_root(self._end)
        if percolates:
            print("Percolates")
        else:
            print("Does Not Percolate")
        return percolates


if __name__ == "__main__":
    p = Percolate(4)
    # p.does_percolate()
    # p.print_percolation_tree()
    # p.union((0, 0), (0, 1))
    # p.print_percolation_tree()
