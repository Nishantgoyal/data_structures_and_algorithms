class Sort:
    def __init__(self, array):
        self._arr = array

    def sort(self):
        return self._subsort(self._arr)

    def _subsort(self, arr):
        l = len(arr)
        mid = l // 2
        if l > 1:
            sort_arr1 = self._subsort(arr[:mid])
            sort_arr2 = self._subsort(arr[mid:])
            sort_arr = self._merge(sort_arr1, sort_arr2)
            return sort_arr
        return arr

    def _merge(self, arr1, arr2):
        arr = []
        l1 = len(arr1)
        l2 = len(arr2)
        i = 0
        j = 0
        while i < l1 and j < l2:
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        while i < l1:
            arr.append(arr1[i])
            i += 1
        while j < l2:
            arr.append(arr2[j])
            j += 1
        return arr
