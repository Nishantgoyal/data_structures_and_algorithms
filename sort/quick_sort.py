class Sort:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        l = len(self.arr)
        # Initially left = 0 and right = 1
        self.quick_sort(0, l - 1)

    def quick_sort(self, left, right):
        # print("\tquicksort {} {}".format(left, right))
        # print("\tArray: {}".format(self.arr))
        if left >= right:
            return
        j = self.partition(left, right)
        self.quick_sort(left, j - 1)
        self.quick_sort(j + 1, right)

    def partition(self, left, right):
        # print("\t\tpartition: Partitioning with left:{} and right:{}".format(left, right))
        ele = self.arr[left]
        # print("\t\tpartition: Choosen element to partition is: {}".format(ele))
        i = left + 1
        j = right
        while True:
            # print("\t\tpartition: Array: {}".format(self.arr))
            # print("\tpartition: i:{} j:{}".format(i, j))
            # print("\tpartition: left:{} right:{}".format(left, right))
            if i > j:
                break
            if self.arr[i] <= ele:
                # print("\tpartition: Incrementing i:{}".format(i))
                i += 1
                continue
            if self.arr[j] > ele:
                # print("\tpartition: Decrementing j:{}".format(j))
                j -= 1
                continue
            if self.arr[i] > ele and self.arr[j] <= ele:
                self.swap(i, j)
        self.swap(left, j)
        return j

    def swap(self, i, j):
        # print("\t\t\tSwapping ele {} at pos {} and ele {} at pos {}".format(
        #     self.arr[i], i, self.arr[j], j))
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        # print("\t\t\tArray after swap: {}".format(self.arr))
