class Sort:
    def __init__(self, array):
        self._arr = array

    def sort(self):
        self.sub_sort(0, len(self._arr) - 1)
        return self._arr

    def sub_sort(self, i, j):
        print("{} {}".format(i, j))
        ele = self._arr[i]
        i_orig, j_orig = i, j
        i += 1
        if j_orig - i_orig <= 1:

        while i < j:
            if self._arr[i] <= ele:
                i += 1
            elif self._arr[j] >= ele:
                j -= 1
            elif self._arr[i] > ele > self._arr[j]:
                self._arr[i], self._arr[j] = self._arr[j], self._arr[i]
        self._arr[i_orig], self._arr[i -
                                     1] = self._arr[i - 1], self._arr[i_orig]
        if i-2 > i_orig:
            self.sub_sort(i_orig, i - 2)
        if i < j_orig:
            self.sub_sort(i, j_orig)
