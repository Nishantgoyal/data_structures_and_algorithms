from random import randint, seed
import time
import math


# from insertion_sort import Sort
# from bubble_sort import Sort
# from selection_sort import Sort
# from shell_sort import Sort
# from merge_sort import Sort
from quick_sort import Sort


def main():
    bound = 30
    arr_size = 1
    last_duration = 0
    ratio = 1
    # seed(bound)
    while True:
        arr = [randint(-1 * bound, bound) for _ in range(arr_size)]
        # arr = list(set(arr))
        s = Sort(arr)

        print(s.arr)
        start = time.time()
        s.sort()
        duration_in_sec = time.time() - start
        print(s.arr)

        if last_duration != 0:
            ratio = duration_in_sec / last_duration
        last_duration = duration_in_sec

        print("{}".format("<") * 10, "{}".format("==")
              * 10, "{}".format(">") * 10)
        print("Array Size: {}".format(len(arr)))
        print("Duration: {:3f}".format(duration_in_sec))
        print("Ratio: {:.3f}".format(math.log2(ratio)))
        arr_size *= 2
        time.sleep(5)


if __name__ == "__main__":
    main()
