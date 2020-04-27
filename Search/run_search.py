import time
from random import randint

# from brute_search import Search
from binary_search import Search


def main():
    arr_size = 2
    ratio = 0
    last = 0
    count = 100
    search = Search()
    rand_range = 50000
    while True:
        arr = sorted([randint(-1 * rand_range, rand_range)
                      for _ in range(arr_size)])
        # print(arr)
        durations = []
        for _ in range(count):
            ele = randint(-1 * rand_range, rand_range)
            # print(ele)
            start = time.time()
            search.search(arr, ele)
            duration = (time.time() - start) * 1000
            durations.append(duration)
        duration = float(sum(durations) / count)
        if last != 0:
            ratio = duration / last
        last = duration
        print("Time taken to search in array of size: {} is {:.3f}ms with ratio: {:.3f}".format(
            arr_size, duration, ratio))
        arr_size *= 2
        # break
    pass


if __name__ == "__main__":
    main()
