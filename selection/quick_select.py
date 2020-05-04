class Select:
    def __init__(self, array):
        self.arr = array

    def select(self, k):
        ''' To find the kth element of the array '''
        left = 0
        right = len(self.arr) - 1
        if k > right + 1:
            raise ("Value of k should be less than or equal to length of array")
        if k < 0:
            raise ("k cannot be negative")
        while left <= right:
            # This will put A[left] at jth place and for all i < j A[i] <= A[j] and for all i > j A[i] > A[j]
            j = self.partition(left, right)
            if j == k:
                return self.arr[j]
            if j < k:
                left = j + 1
                k = k - j
            else:
                right = j - 1

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


if __name__ == "__main__":
    arr = ["3", "43", "23", "56", "57", "72"]
    s = Select(arr)
    print(s.select(2))
p