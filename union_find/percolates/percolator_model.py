import random
import sys
import numpy as np


class Percolate:
    def __init__(self, n):
        '''
            Input:
                n: dimension of lattice
        '''
        self._N = n
        self._start = (-1, -1)
        self._percolate_tree = [[0 for _ in range(n)]
                                for _ in range(n)]
        self._lattice = [[(j, i) for i in range(n)]
                         for j in range(n)]
        self._end = (n, n)
        # self.print_percolation_tree()
        # self.join_start_end_nodes()
        # self.print_percolation_tree()

    # def join_start_end_nodes(self):
    #     for node in self._lattice[0][1:]:
    #         self.union(self._lattice[0][0], node)
    #     for node in self._lattice[-1][:-1]:
    #         self.union(self._lattice[-1][-1], node)

    def _get_root(self, ele):
        while ele != self._lattice[ele[0]][ele[1]]:
            ele = self._lattice[ele[0]][ele[1]]
        return ele

    def union(self, a, b):
        '''
            It connects set containing element `a` to set containing element `b`
        '''
        # print("U {} {}".format(a, b))
        root_a = self._get_root(a)
        root_b = self._get_root(b)
        self._lattice[root_a[0]][root_a[1]] = root_b

    def print_percolation_tree(self):
        print("********" * self._N)
        print(self._start)
        for ele in self._lattice:
            print(ele)
        print(self._end)
        print()
        for ele in self._percolate_tree:
            print(ele)
        print("********" * self._N)

    def does_percolate(self):
        if self._start == (-1, -1) or self._end == (self._N, self._N):
            return False
        percolates = self._get_root(self._start) == self._get_root(self._end)
        # if percolates:
        #     print("Percolates")
        # else:
        #     print("Does Not Percolate")
        return percolates

    def choose_cell(self):
        r = random.randrange(0, self._N ** 2)
        y = r % self._N
        x = (r - y) // self._N
        return x, y

    def get_percolation_threshold(self):
        return float(sum([sum(l) for l in self._percolate_tree]) / self._N ** 2)

    def get_adjacent_cells(self, x, y):
        return[
            (x - 1, y),
            (x, y - 1),
            (x + 1, y),
            (x, y + 1),
        ]

    def is_valid_cell(self, ele):
        return ele[0] >= 0 and ele[1] >= 0 and ele[0] < self._N and ele[1] < self._N

    def create_open_cell(self, cell):
        x, y = cell
        self._percolate_tree[x][y] = 1
        if x == 0 and self._start == (-1, -1):
            self._start = (x, y)
        if x == (self._N - 1) and self._end == (self._N, self._N):
            self._end = (x, y)
        neighbours = list(
            filter(self.is_valid_cell, self.get_adjacent_cells(x, y)))
        for n in neighbours:
            if self._percolate_tree[n[0]][n[1]] == 1:
                self.union(n, (x, y))


if __name__ == "__main__":
    n = int(sys.argv[1])
    T = int(sys.argv[2])
    ratios = []
    for t in range(T):
        p = Percolate(n)
        while not p.does_percolate():
            x, y = p.choose_cell()
            if p._percolate_tree[x][y] == 1:
                continue
            p.create_open_cell((x, y))
        ratio = p.get_percolation_threshold()
        print("Trial {} succeeded with percolation ratio: {}".format(t, ratio))
        ratios.append(ratio)
    mean = np.mean(ratios)
    std = np.std(ratios)
    print("Ratio Stats: Mean: {}\tStd Deviation: {}".format(mean, std))


'''
p.does_percolate()
print(p.get_percolation_threshold())
p.print_percolation_tree()
p.union((0, 0), (0, 1))
p.print_percolation_tree()
'''
