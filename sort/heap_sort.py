import sys


class Sort:

    class BinaryHeap:
        def __init__(self):
            self._heap = []
            self._heap_len = len(self._heap)

        def create_heap(self, arr):
            # print("Creating heap with Arr:{}".format(arr))
            for ele in arr:
                self.insert_item(ele)

        def insert_item(self, ele):
            # print("\tInserting {}".format(ele))
            self._heap.append(ele)
            self.swim(self._heap_len)
            self._heap_len += 1

        def swim(self, index_ele):
            # print("\t\tSwimming {} at {}".format(
            #     self._heap[index_ele], index_ele))
            index_par = (index_ele - 1) // 2
            if self._heap[index_ele] < self._heap[index_par]:
                self._heap[index_ele], self._heap[index_par] = self._heap[index_par], self._heap[index_ele]
                if index_par > 0:
                    self.swim(index_par)

        def sink(self, index_ele):
            # print("Sinking {}".format(index_ele))

            index_fc = 2 * (index_ele + 1) - 1
            index_sc = 2 * (index_ele + 1)
            max_index = index_ele
            max_value = self._heap[index_ele]

            if index_fc < self._heap_len:
                if self._heap[index_fc] < max_value:
                    max_index = index_fc
                    max_value = self._heap[index_fc]
            if index_sc < self._heap_len:
                if self._heap[index_sc] < max_value:
                    max_value = self._heap[index_sc]
                    max_index = index_sc

            if index_ele != max_index:
                self._heap[index_ele], self._heap[max_index] = self._heap[max_index], self._heap[index_ele]
                self.sink(max_index)

        def get_ele(self):
            if self._heap_len <= 0:
                # print("Empty Heap...")
                return
            ele = self._heap[0]
            self._heap_len -= 1
            self._heap[0] = self._heap[self._heap_len]
            self.sink(0)
            self._heap.pop(self._heap_len)
            return ele

    def __init__(self, array):
        self.arr = array
        self._heap = self.BinaryHeap()

    def sort(self):
        self._heap.create_heap(self.arr)
        for i in range(len(self.arr)):
            self.arr[i] = self._heap.get_ele()
