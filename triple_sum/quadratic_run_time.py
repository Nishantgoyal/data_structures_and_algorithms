import json


class TripleSum:
    def __init__(self, arr):
        self.arr = sorted([i for i in arr])

    def is_triple_sum(self, x, y, z):
        return x + y + z == 0

    def find_triple_sums(self):
        triple_sums = []
        l = len(self.arr)
        for i in range(l - 2):
            x = self.arr[i]
            low = i + 1
            high = l - 1
            while low < high:
                y = self.arr[low]
                z = self.arr[high]
                s = x + y + z
                if s > 0:
                    high -= 1
                elif s == 0:
                    low += 1
                    high -= 1
                    triple_sums.append((x, y, z))
                else:
                    low += 1
        return len(triple_sums)
