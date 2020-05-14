import sys


class BinaryHeap:
    def __init__(self, type="Max"):
        self._type = type
        self._heap = []
        self._heap_len = len(self._heap)

    def create_heap(self, arr):
        print("Creating heap with Arr:{} of type: {}".format(arr, self._type))
        for ele in arr:
            self.insert_item(ele)

    def insert_item(self, ele):
        print("\tInserting {}".format(ele))
        self._heap.append(ele)
        self.swim(self._heap_len)
        self._heap_len += 1

    def swim(self, index_ele):
        print("\t\tSwimming {} at {}".format(self._heap[index_ele], index_ele))
        index_par = (index_ele - 1) // 2
        if self._type == "Max":
            if self._heap[index_ele] > self._heap[index_par]:
                self._heap[index_ele], self._heap[index_par] = self._heap[index_par], self._heap[index_ele]
                if index_par > 0:
                    self.swim(index_par)
        else:
            if self._heap[index_ele] < self._heap[index_par]:
                self._heap[index_ele], self._heap[index_par] = self._heap[index_par], self._heap[index_ele]
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
        print("Sinking {}".format(index_ele))

        index_fc = 2 * (index_ele + 1) - 1
        index_sc = 2 * (index_ele + 1)
        max_index = index_ele
        max_value = self._heap[index_ele]

        if index_fc < self._heap_len:
            if self._type == "Max":
                if self._heap[index_fc] > max_value:
                    max_index = index_fc
                    max_value = self._heap[index_fc]
            if self._type == "Min":
                if self._heap[index_fc] < max_value:
                    max_index = index_fc
                    max_value = self._heap[index_fc]
        if index_sc < self._heap_len:
            if self._type == "Max":
                if self._heap[index_sc] > max_value:
                    max_value = self._heap[index_sc]
                    max_index = index_sc
            if self._type == "Min":
                if self._heap[index_sc] < max_value:
                    max_value = self._heap[index_sc]
                    max_index = index_sc

        if index_ele != max_index:
            self._heap[index_ele], self._heap[max_index] = self._heap[max_index], self._heap[index_ele]
            self.sink(max_index)

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

    heap_type = ""
    while heap_type not in ["Max", "Min"]:
        print("Please Enter the Type of heap. (Max/Min). Enter 'X' to Exit")
        heap_type = input()
        if heap_type == "X":
            sys.exit()
        if heap_type not in ["Max", "Min"]:
            print("Invalid Type. Please retry.")

    heap = BinaryHeap(heap_type)
    heap.print_heap()

    while True:
        print("Enter Choice: (I: Insert Ele, G: Get top element, X: Exit")
        inp = input()
        if inp not in ["I", "G", "X"]:
            print("Invalid Input. Please retry.")
            continue
        if inp == "I":
            print("Enter integer to insert")
            try:
                val = int(input())
                heap.insert_item(val)
                heap.print_heap()
            except Exception as ex:
                print("Exception {}".format(ex))
                print("Invalid data. Please retry.")
            continue
        if inp == "G":
            ele = heap.get_ele()
            print("{} element is {}".format(heap_type, ele))
            heap.print_heap()
            continue
        if inp == "X":
            sys.exit()
