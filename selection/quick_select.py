class Select:
    def __init__(self, array):
        self.arr = array

    def select(self, k):
        ''' 
            To find the kth largest element of the array.
            This will be the arr[-k] element in sorted array.
        '''
        k = k - 1
        left = 0
        right = len(self.arr) - 1
        if k > right:
            raise ("Value of k should be less than or equal to length of array")
        if k < 0:
            raise ("k cannot be negative or zero")
        while left <= right:
            # print("In Select loop with left:{} and right:{} and k:{}".format(
            #     left, right, k))
            # This will put A[left] at jth place and for all i < j A[i] <= A[j] and for all i > j A[i] > A[j]
            j = self.partition(left, right)
            # print("value of j:{} returned".format(j))
            if j == k:
                return self.arr[j]
            if j < k:
                left = j + 1
                # k = k - j
            else:
                right = j - 1

    def swap(self, i, j):
        # print("\t\tSwapping ele A[i]: {} at i: {} and ele A[j] {} at j: {}".format(
        #     self.arr[i], i, self.arr[j], j))
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        # print("\t\tArray after swap: {}".format(self.arr))

    def partition(self, left, right):
        '''
            It shall take the arr[left] element and put it at jth index, such that, all arr[i] <= arr[j] for i < j and all arr[k] > arr[j] for k > j
        '''
        # print("In Partition...")
        # ele = self.arr[left]
        i = left + 1
        j = right
        while True:
            # print("\tArray:{}".format(self.arr))
            # print("\ti:{} j:{}".format(i, j))
            # print("\tleft:{} right:{}".format(left, right))
            # print(self.arr[left])
            # print("true")
            # if i >= j:
            # break
            # i += 1
            while i < right and self.arr[i] < self.arr[left]:
                # print("\tIncrementing i:{}".format(i))
                i += 1
                if i == right:
                    break
            while j > left and self.arr[j] > self.arr[left]:
                # print("\tReducing j:{}".format(j))
                j -= 1
                if j == left:
                    break
            if i >= j:
                break
            self.swap(i, j)
        self.swap(left, j)
        return j


if __name__ == "__main__":
    arr = [3, 43, 23, 56, 57, 72]
    s = Select(arr)
    print(s.select(3))
