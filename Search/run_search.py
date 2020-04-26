import time
from random import randint

from brute_search import Search


def main():
    arr_size = 2
    ratio = 0
    last = 0
    count = 100
    search = Search()
    while True:
        arr = [randint(-20000, 20000) for _ in range(arr_size)]
        durations = []
        for _ in range(count):
            ele = randint(-20000, 20000)
            start = time.time()
            search.search(arr, ele)
            duration = (time.time() - start) * 1000
            durations.append(duration)
        duration = float(sum(durations) / count)
        if last != 0:
            ratio = duration / last
        last = duration
        print("Time taken to search in array of size: {} is {:.3f} with ratio: {:.3f}".format(
            arr_size, duration, ratio))
        arr_size *= 2
    pass


if __name__ == "__main__":
    main()
