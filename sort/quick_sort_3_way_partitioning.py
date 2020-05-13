class Sort:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        l = len(self.arr)
        # Initially left = 0 and right = l - 1
        self.quick_sort(0, l - 1)

    def quick_sort(self, left, right):
        # print("quicksort {} {}".format(left, right))
        # print("Array:{}".format(self.arr))
        if left >= right:
            return
        i, j = self.partition(left, right)
        self.quick_sort(left, i - 1)
        self.quick_sort(j + 1, right)

    def partition(self, left, right):
        # print("\tPartitioning --> left:{} right:{}".format(left, right))
        i = left + 1
        while True:
            # print("\tArray:{}".format(self.arr))
            # print("\tleft:{} i:{} right:{}".format(left, i, right))
            if i > right:
                break
            if self.arr[i] < self.arr[left]:
                # print("\tIncrementing left and i, and swapping i and left")
                self.swap(left, i)
                left += 1
                i += 1
                continue
            if self.arr[i] == self.arr[left]:
                # print("\tIncrementing i")
                i += 1
                continue
            if self.arr[i] > self.arr[left]:
                # print("\tDecrementing right and swapping i with right")
                self.swap(right, i)
                right -= 1
                continue
        return (left, right)

    def swap(self, i, j):
        # print("\t\tSwapping ele {} at pos {} and ele {} at pos {}".format(
        #     self.arr[i], i, self.arr[j], j))
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        # print("\t\tArray after swap: {}".format(self.arr))


if __name__ == "__main__":
    arr = [3, 4, 3, 6, 7, 2, 1, 5, 3, 6]
    s = Sort(arr)
    s.sort()
    print(s.arr)
