class Search:

    def search(self, arr, ele):
        low = 0
        high = len(arr) - 1
        found = False
        while low <= high:
            mid = int((low + high) / 2)
            if arr[mid] == ele:
                found = True
            if arr[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return found
