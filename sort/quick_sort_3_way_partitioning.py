class Sort:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        l = len(self.arr)
        # Initially left = 0 and right = l - 1
        self.sub_sort(0, l - 1)

    def sub_sort(self, left, right):
        print("subsort {} {}".format(left, right))
        print("Array:{}".format(self.arr))
        if left >= right:
            return
        j = self.partition(left, right)
        self.sub_sort(left, j - 1)
        self.sub_sort(j + 1, right)
        # print(self.arr)

    def partition(self, left, right):
        print("\tPartitioning --> left:{} right:{}".format(left, right))
        i = left + 1
        # j = right
        while True:
            print("\tArray:{}".format(self.arr))
            print("\tleft:{} i:{} right:{}".format(left, i, right))
            if i >= right:
                break
            if self.arr[i] < self.arr[left]:
                print("Incrementing left and i, and swapping i and left")
                self.swap(left, i)
                left += 1
                i += 1
                continue
            if self.arr[i] > self.arr[left]:
                print("Decrementing right and swapping i and right")
                self.swap(right, i)
                right -= 1
                continue
            if self.arr[i] == self.arr[left]:
                print("Incrementing i")
                i += 1
                continue
            # while i < right and self.arr[i] < self.arr[left]:
            #     print("\tIncrementing i:{}".format(i))
            #     i += 1
            #     if i == right:
            #         break
            # while j > left and self.arr[j] > self.arr[left]:
            #     print("\tDecrementing j:{}".format(j))
            #     j -= 1
            #     if j == left:
            #         break
            # if i >= j:
            #     break
            # self.swap(i, j)
        # self.swap(left, j)
        return (left, right)

    def swap(self, i, j):
        print("\t\tSwapping ele A[i]: {} at i: {} and ele A[j] {} at j: {}".format(
            self.arr[i], i, self.arr[j], j))
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        print("\t\tArray after swap: {}".format(self.arr))


if __name__ == "__main__":
    arr = [3, 4, 3, 6, 7, 2, 1, 5, 3, 6]
    s = Sort(arr)
    s.sort()
    print(s.arr)
