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

    def count_triple_sums(self):
        count = 0
        s = Search()
        l = len(self.arr)
        for i in range(l):
            for j in range(i + 1, l):
                val = -1 * (self.arr[i] + self.arr[j])
                if s.search(self.arr[j+1:l], val):
                    count += 1
        return count

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
        return triple_sums

    def save_triple_sums(self, triple_sums, duration):
        file_name = __file__.split(".")[0] + ".json"
        out = {}
        out["count_of_triple_sums"] = str(len(triple_sums))
        out["duration"] = str(duration)
        out["arr"] = ", ".join([str(ele) for ele in self.arr])
        out["triple_sums"] = [", ".join([str(i) for i in t])
                              for t in triple_sums]
        with open(file_name, "w") as f:
            json.dump(out, f, indent=4)

    def save_triple_count(self, triple_count, duration):
        file_name = __file__.split(".")[0] + ".json"
        out = {}
        out["count"] = str(triple_count)
        out["duration"] = str(duration)
        out["arr"] = ", ".join([str(ele) for ele in self.arr])
        with open(file_name, "w") as f:
            json.dump(out, f, indent=4)
