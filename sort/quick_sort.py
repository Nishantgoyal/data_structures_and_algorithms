class Sort:
    def __init__(self, array):
        self.arr = array

    def sort(self):
        self.sub_sort(0, len(self.arr) - 1)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def partition(self, left, right):
        i = left
        j = right + 1
        while True:
            i += 1
            while self.arr[i] < self.arr[left]:
                i += 1
                if i == right:
                    break
            j -= 1
            while self.arr[j] > self.arr[left]:
                j -= 1
                if j == left:
                    break
            if i >= j:
                break
            self.swap(i, j)
        self.swap(left, j)
        return j

    def sub_sort(self, left, right):
        if left >= right:
            return
        j = self.partition(left, right)
        self.sub_sort(left, j - 1)
        self.sub_sort(j + 1, right)
