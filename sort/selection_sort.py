class Sort:
    def __init__(self, array):
        self._arr = array

    def sort(self):
        l = len(self._arr)
        for i in range(l-1):
            min_ele = self._arr[i]
            min_ind = i
            for j in range(i, l):
                if self._arr[j] < min_ele:
                    min_ele = self._arr[j]
                    min_ind = j
            if i != min_ind:
                self._arr[min_ind] = self._arr[i]
                self._arr[i] = min_ele
