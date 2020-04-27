import json


class TripleSum:
    def __init__(self, arr):
        self.arr = sorted([i for i in arr])

    def is_triple_sum(self, x, y, z):
        return x + y + z == 0

    def find_triple_sums(self):
        triple_sums = []
        l = len(self.arr)
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if self.is_triple_sum(self.arr[i], self.arr[j], self.arr[k]):
                        triple_sums.append(
                            (self.arr[i], self.arr[j], self.arr[k]))
        return len(triple_sums)
