from random import randint, seed
import time
import math


# from insertion_sort import Sort
# from bubble_sort import Sort
# from selection_sort import Sort
# from shell_sort import Sort
# from merge_sort import Sort
from quick_sort import Sort
# from quick_sort_3_way_partitioning import Sort
# from heap_sort import Sort
# from heap_sort_v2 import Sort


def run_single_test():
    bound = 30
    arr_size = 10
    # seed(bound)
    arr = [randint(0, bound) for _ in range(arr_size)]
    print("Initialised Array: {}..!!".format(arr))
    s = Sort(arr)
    s.sort()
    print(s.arr)


def run_tests():
    bound = 3000000
    arr_size = 1
    last_duration = 0
    ratio = 1.0
    while True:
        print("{}".format("<") * 10, "{}".format("==")
              * 10, "{}".format(">") * 10)
        arr = [randint(-1 * bound, bound) for _ in range(arr_size)]
        print("Initialised Array of size: {}..!!".format(arr_size))
        s = Sort(arr)

        start = time.time()
        s.sort()
        duration_in_sec = time.time() - start

        if last_duration != 0:
            ratio = duration_in_sec / last_duration
        last_duration = duration_in_sec

        print("Duration: {:3f}".format(duration_in_sec))
        print("Ratio: {:.3f}".format(math.log2(ratio)))
        arr_size *= 2
        # time.sleep(5)


def main():
    run_tests()
    # run_single_test()


if __name__ == "__main__":
    main()
