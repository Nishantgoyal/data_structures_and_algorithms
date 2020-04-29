import math
import random


class Sort:
    def __init__(self, array):
        self._arr = array

    def _get_h(self, N):
        l2n = math.log2(N)
        h = 2 ** math.ceil(l2n)
        while(h > 1):
            h = int(h / 2)
            yield h

    def sort(self):
        l = len(self._arr)
        for h in self._get_h(l):
            for i in range(h, l):
                j = i
                while (j - h) >= 0:
                    if self._arr[j] < self._arr[j - h]:
                        self._arr[j], self._arr[j -
                                                h] = self._arr[j - h], self._arr[j]
                    else:
                        break
                    j -= h
