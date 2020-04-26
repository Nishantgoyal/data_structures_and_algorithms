import json


class TripleSum:
    def __init__(self, arr):
        self.arr = [i for i in arr]

    def is_triple_sum(self, x, y, z):
        return x + y + z == 0

    def count_triple_sums(self):
        count = 0
        l = len(self.arr)
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if self.is_triple_sum(self.arr[i], self.arr[j], self.arr[k]):
                        count += 1
        return count

    def find_triple_sums(self):
        triple_sums = []
        l = len(self.arr)
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if self.is_triple_sum(self.arr[i], self.arr[j], self.arr[k]):
                        triple_sums.append(
                            (self.arr[i], self.arr[j], self.arr[k]))
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
