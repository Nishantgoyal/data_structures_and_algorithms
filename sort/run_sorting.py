from random import randint
import time
import math


from insertion_sort import Sort


def main():
    bound = 20000
    arr_size = 2
    last_duration = 0
    ratio = 1
    while True:
        arr = [randint(-1 * bound, bound) for _ in range(arr_size)]
        s = Sort(arr)

        start = time.time()
        s.sort()
        duration_in_sec = time.time() - start

        if last_duration != 0:
            ratio = duration_in_sec / last_duration
        last_duration = duration_in_sec

        print("{}".format("<") * 10, "{}".format("==")
              * 10, "{}".format(">") * 10)
        print("Array Size: {}".format(len(arr)))
        print("Duration: {:3f}".format(duration_in_sec))
        print("Ratio: {:.3f}".format(math.log2(ratio)))
        arr_size *= 2


if __name__ == "__main__":
    main()
