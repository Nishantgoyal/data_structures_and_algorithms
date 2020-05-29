import sys
import json
import time
import math

'''
    A taxicab number is an integer that can be expressed as the sum of two cubes of positive integers in two different ways. 
    a**3 + b**3 = c**3 + d**3 = taxicab_number
    E.g., 9**3 + 10**3 = 1**3 + 12**3 = 1729

    Find all taxicab numbers with a,b,c,d < n
'''


class TaxiCabNumber:
    def __init__(self, n):
        self._n = n

    def generate_numbers(self):
        for i in range(self._n):
            for j in range(i, self._n):
                if i != j:
                    # print(i, j)
                    yield (i ** 3 + j ** 3, i, j)

    def get_taxicabs(self):
        all_data = {}
        taxicabs = {}
        for num, i, j in self.generate_numbers():
            if num not in all_data:
                all_data[num] = ["{},{}".format(i, j)]
            else:
                all_data[num].append("{},{}".format(i, j))
                taxicabs[num] = [ele for ele in all_data[num]]
        # return taxicabs

    def dump_taxicabs(self):
        data = self.get_taxicabs()
        file_name = "{}.json".format(__file__.split(".")[0])
        with open(file_name, "w") as f:
            json.dump(data, f, indent=2)
        # return list(data.keys())


def run_tests():
    N = 1
    # arr_size = 1
    last_duration = 0
    ratio = 1.0
    while True:
        print("{}".format("<") * 10, "{}".format("==")
              * 10, "{}".format(">") * 10)
        print("N: {}".format(N))
        tc = TaxiCabNumber(N)

        start = time.time()
        tc.get_taxicabs()
        duration_in_sec = time.time() - start

        if last_duration != 0:
            ratio = duration_in_sec / last_duration
        last_duration = duration_in_sec

        print("Duration: {:3f}".format(duration_in_sec))
        print("Ratio: {:.3f}".format(math.log2(ratio)))
        N *= 2
        # time.sleep(5)


if __name__ == "__main__":
    run_tests()
