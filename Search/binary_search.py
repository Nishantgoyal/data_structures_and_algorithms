class Search:

    def search(self, arr, ele):
        low = 0
        high = len(arr)
        found = False
        while low < high:
            mid = int((low + high) / 2)
            # print("{} {} {} --> {}".format(low, mid, high, arr[mid]))
            if arr[mid] == ele:
                found = True
            if arr[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return found
