import random
import sys
import time
import math

from triple_sum_with_binary_search import TripleSum
# from brute_force import TripleSum


def gen_random_arr(size):
    bound = 20000
    arr = [random.randint(-1 * bound, bound)
           for i in range(size)]
    return arr


def run_triple_sum():
    last = 0
    ratio = 1
    i = 1
    random.seed(200)
    while True:
        arr = list(set(gen_random_arr(i)))
        ts = TripleSum(arr)
        start_time = time.time()
        count = ts.count_triple_sums()
        duration = time.time() - start_time
        if last != 0:
            ratio = duration / last
        last = duration
        print("\nsize:\t\t{}\nduration:\t{:.3f}s\ncount:\t\t{}\nlog_ratio:\t{}".format(
            i, duration, count, math.log2(ratio)))
        print("<<<<<<<<<<<<===============>>>>>>>>>>>>")
        i *= 2


if __name__ == "__main__":
    run_triple_sum()
