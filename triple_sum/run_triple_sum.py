import random
import sys
import time
# import timeit

from brute_force import TripleSum


def gen_random_arr(bound):
    arr = [random.randint(-1 * bound, bound)
           for i in range(-1 * bound, bound)]
    return arr


if __name__ == "__main__":
    arr = gen_random_arr(int(sys.argv[1]))
    ts = TripleSum(arr)
    start_time = time.time()
    triple_sums = ts.find_triple_sums()
    duration = time.time() - start_time
    ts.save_triple_sums(triple_sums, duration)
