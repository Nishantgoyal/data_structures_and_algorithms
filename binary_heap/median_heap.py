import sys
from random import randint, seed


class MedianHeap:
    def __init__(self):
        self._heap = []
        self._heap_len = len(self._heap)

    def create_heap(self, arr):
        print("Creating heap with Arr:{}".format(arr))
        for ele in arr:
            self.insert_item(ele)
            self.print_heap()

    def is_left(self, index):
        return index % 2 == 1

    def insert_item(self, ele):
        print("\tInserting {}".format(ele))
        self._heap.append(ele)
        self.swim(self._heap_len)
        # self.sink(self._heap_len)
        self._heap_len += 1

    def less_than_all_par(self, index):
        index_par = (index - 1) // 2
        while index_par >= 0:
            if self._heap[index] > self._heap[index_par]:
                return False
            index_par = (index_par - 1) // 2
        return True

    def greater_than_all_par(self, index):
        index_par = (index - 1) // 2
        while index_par >= 0:
            if self._heap[index] < self._heap[index_par]:
                return False
            index_par = (index_par - 1) // 2
        return True

    def swim(self, index_ele):
        # print("\t\tSwimming {} at {}".format(self._heap[index_ele], index_ele))
        index_par = (index_ele - 1) // 2
        if self.is_left(index_ele):
            print("\t\tSwimming from left {} at {}".format(
                self._heap[index_ele], index_ele))
            if self.less_than_all_par(index_ele):
                print("\t\tExchanging {} and {}".format(
                    self._heap[index_ele], self._heap[index_par]))
                self._heap[index_ele], self._heap[index_par] = self._heap[index_par], self._heap[index_ele]
                self.sink(index_par)
                if index_par > 0:
                    self.swim(index_par)
        if not self.is_left(index_ele):
            print("\t\tSwimming from right {} at {}".format(
                self._heap[index_ele], index_ele))
            if self.greater_than_all_par(index_ele):
                print("\t\tExchanging {} and {}".format(
                    self._heap[index_ele], self._heap[index_par]))
                self._heap[index_ele], self._heap[index_par] = self._heap[index_par], self._heap[index_ele]
                self.sink(index_par)
                if index_par > 0:
                    self.swim(index_par)

    def print_heap(self):
        heap_string = ""
        heap_print = [[]]
        node_level = 0
        node_count = 0

        for ele in self._heap:
            node_in_current_level = 2 ** node_level
            if node_count >= node_in_current_level:
                node_level += 1
                heap_print.append([])
                node_count = 0
            heap_print[node_level].append(ele)
            node_count += 1

        for heap_level in heap_print:
            for ele in heap_level:
                heap_string += "*" * (2 ** node_level + 1)
                heap_string += str(ele)
                # heap_string += "*" * (2 ** node_level + 1)
            node_level -= 1
            heap_string += "\n"
        print(heap_string)

    def sink(self, index_ele):
        print("\t\tSinking {}".format(index_ele))

        index_left = 2 * (index_ele + 1) - 1
        index_right = 2 * (index_ele + 1)

        if index_left < self._heap_len:
            if self._heap[index_left] > self._heap[index_ele]:
                print("\t\tSinking to Left Exchanging {} and {}".format(
                    self._heap[index_ele], self._heap[index_left]))
                self._heap[index_ele], self._heap[index_left] = self._heap[index_left], self._heap[index_ele]
                self.sink(index_left)
                return
        if index_right < self._heap_len:
            if self._heap[index_right] < self._heap[index_ele]:
                print("\t\tSinking to Right Exchanging {} and {}".format(
                    self._heap[index_ele], self._heap[index_right]))
                self._heap[index_ele], self._heap[index_right] = self._heap[index_right], self._heap[index_ele]
                self.sink(index_right)
                return
        return

    def get_ele(self):
        if self._heap_len <= 0:
            print("Empty Heap...")
            return
        ele = self._heap[0]
        self._heap_len -= 1
        self._heap[0] = self._heap[self._heap_len]
        self.sink(0)
        self._heap.pop(self._heap_len)
        return ele


if __name__ == "__main__":
    seed(20)
    arr = [randint(0, 30) for _ in range(15)]

    # heap_type = ""
    # while heap_type not in ["Max", "Min"]:
    #     print("Please Enter the Type of heap. (Max/Min). Enter 'X' to Exit")
    #     heap_type = input()
    #     if heap_type == "X":
    #         sys.exit()
    #     if heap_type not in ["Max", "Min"]:
    #         print("Invalid Type. Please retry.")

    heap = MedianHeap()
    heap.create_heap(arr)
    heap.print_heap()

    # while True:
    #     print("Enter Choice: (I: Insert Ele, G: Get top element, X: Exit")
    #     inp = input()
    #     if inp not in ["I", "G", "X"]:
    #         print("Invalid Input. Please retry.")
    #         continue
    #     if inp == "I":
    #         print("Enter integer to insert")
    #         try:
    #             val = int(input())
    #             heap.insert_item(val)
    #             heap.print_heap()
    #         except Exception as ex:
    #             print("Exception {}".format(ex))
    #             print("Invalid data. Please retry.")
    #         continue
    #     if inp == "G":
    #         ele = heap.get_ele()
    #         print("{} element is {}".format(heap_type, ele))
    #         heap.print_heap()
    #         continue
    #     if inp == "X":
    #         sys.exit()
