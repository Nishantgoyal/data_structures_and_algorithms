import random
import sys
import time
import math
# import timeit

from brute_force import TripleSum


def gen_random_arr(size):
    bound = 2000
    arr = [random.randint(-1 * bound, bound)
           for i in range(size)]
    return arr


def run_triple_sum():
    last = 0
    ratio = 1
    i = 2
    while True:
        arr = gen_random_arr(i)
        ts = TripleSum(arr)
        start_time = time.time()
        count = ts.count_triple_sums()
        duration = time.time() - start_time
        if last != 0:
            ratio = duration / last
        last = duration
        # ts.save_triple_count(count, duration)
        print("For \n\tsize:\t\t{}\n\tcount:\t\t{}\n\tduration:\t{:.3f}\n\tlog_ratio:\t{}".format(
            i, count, duration, math.log2(ratio)))
        i *= 2


if __name__ == "__main__":
    run_triple_sum()
