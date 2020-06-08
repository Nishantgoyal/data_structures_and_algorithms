import copy
import time
import json
import sys
from random import randint

from largest_numbers import LargestNumber
from largest_numbers_brute import LargestNumberBrute
from permutations import Permutations


def get_arr():
    arr_size = randint(2, 5)

    ele_upper_bound = 200
    arr = [
        randint(2, ele_upper_bound)
        for _ in range(arr_size)
    ]
    # arr = [14, 3, 186, 143, 119]
    # arr = [26, 141, 2, 93]
    # arr = [191, 107, 19, 136, 35]
    # arr = [124, 118, 16, 165, 181, 182, 43, 18, 55, 112]
    # arr = [3,9,5,9,7,1]
    return arr


def run_test():
    arr = get_arr()

    print("Array: {}".format(arr))

    # # Brute Force
    largest_brute = LargestNumberBrute(arr)
    largest_number_brute = largest_brute.find_largest_number()

    # # Original Algo
    largest = LargestNumber(arr)
    largest_number = largest.find_largest_number()

    compare_results(largest_number, largest_number_brute)
    print("Largest Number: {}".format(largest_number))

    # permutations = Permutations()
    # permutations.test()


def compare_results(brute_result, algo_result):
    if brute_result != algo_result:
        print("****Error****")
        print("Brute Result: {}".format(algo_result))
        print("Algo Result: {}".format(brute_result))
        print(type(brute_result))
        print(type(algo_result))
        sys.exit()


def stress_test():
    while True:
        run_test()
        time.sleep(1)


if __name__ == "__main__":
    run_test()
    stress_test()
