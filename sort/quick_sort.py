class Sort:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        self.sub_sort(0, len(self.arr) - 1)

    def swap(self, i, j):
        # print("Swapping ele A[i]: {} at i: {} and ele A[j] {} at j: {}".format(
        #     self.arr[i], i, self.arr[j], j))
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        # print("Array after swap: {}".format(self.arr))

    def partition(self, left, right):
        i = left
        j = right + 1
        while True:
            # print(self.arr)
            # print(i, j)
            # print(left, right)
            # print(self.arr[left])
            # print("true")
            # if i >= j:
            #     break
            i += 1
            if i < right:
                while self.arr[i] < self.arr[left]:
                    # print("i:{}".format(i))
                    i += 1
                    if i == right:
                        break
            j -= 1
            if j > left:
                while self.arr[j] > self.arr[left]:
                    # print("j:{}".format(j))
                    j -= 1
                    if j == left:
                        break
            if i >= j:
                break
            self.swap(i, j)
        self.swap(left, j)
        return j

    def sub_sort(self, left, right):
        # print("subsort {} {}".format(left, right))
        # print(self.arr)
        if left >= right:
            return
        j = self.partition(left, right)
        self.sub_sort(left, j - 1)
        self.sub_sort(j + 1, right)
        # print(self.arr)
