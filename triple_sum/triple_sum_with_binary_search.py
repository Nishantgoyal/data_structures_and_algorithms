import json


class Search:

    def search(self, arr, ele):
        low = 0
        high = len(arr) - 1
        found = False
        while low <= high and not found:
            mid = int((low + high) / 2)
            if arr[mid] == ele:
                return True
            if arr[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return found


class TripleSum:
    def __init__(self, arr):
        self.arr = sorted([i for i in arr])

    def is_triple_sum(self, x, y, z):
        return x + y + z == 0

    def find_triple_sums(self):
        triple_sums = []
        l = len(self.arr)
        s = Search()
        for i in range(l):
            x = self.arr[i]
            for j in range(i + 1, l):
                y = self.arr[j]
                val = -1 * (x + y)
                present = s.search(self.arr[j+1:l], val)
                if present:
                    triple_sums.append((x, y, val))
        return len(triple_sums)
