class Sort:
    def __init__(self, array):
        self._arr = array

    def sort(self):
        l = len(self._arr)
        for _ in range(0, l - 1):
            is_sorted = True
            for j in range(0, l - 1):
                if self._arr[j] > self._arr[j+1]:
                    is_sorted = False
                    self._arr[j], self._arr[j +
                                            1] = self._arr[j + 1], self._arr[j]
            if is_sorted:
                break
