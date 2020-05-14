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
        index_par = index_ele // 2
        if self._type == "Max":
            if self._heap[index_ele] > self._heap[index_par]:
                self._heap[index_ele], self._heap[index_par] = self._heap[index_par], self._heap[index_ele]
                self.swim(index_par)
        else:
            if self._heap[index_ele] < self._heap[index_par]:
                self._heap[index_ele], self._heap[index_par] = self._heap[index_par], self._heap[index_ele]
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
            heap_string += "\n"
            for ele in heap_level:
                heap_string += "*" * (2 ** node_level + 1)
                heap_string += str(ele)
                heap_string += "*" * (2 ** node_level + 1)
            node_level -= 1
        print(heap_string)

    def get_ele(self):
        pass


if __name__ == "__main__":
    arr = [54, 65, 32, 89, 56, 3, 84, 24, 57, 25, 86, 64, 27]
    # print(arr)
    heap = BinaryHeap()
    heap.create_heap(arr)
    heap.print_heap()
