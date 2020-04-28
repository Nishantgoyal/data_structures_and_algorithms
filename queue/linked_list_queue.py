
class Queue:
    class _Node:
        def __init__(self, item):
            self.item = item
            self.next_node = None

    def __init__(self):
        self._queue = None
        self._queue_end = None

    def enqueue(self, ele):
        ''' Enqueue in the end '''
        print("Enqueuing element: {}".format(ele))
        n = self._Node(ele)
        if self._queue is None:
            self._queue = n
            self._queue_end = n
            return

        self._queue_end.next_node = n
        self._queue_end = self._queue_end.next_node
        # if self._queue is None:
        #     self._queue = n
        #     return
        # while temp.next_node is not None:
        #     temp = temp.next_node
        # temp.next_node = n

    def dequeue(self):
        if self._queue is None:
            return None
        ele = self._queue.item
        self._queue = self._queue.next_node
        print("Dequeued Element: {}".format(ele))
        return ele

    def is_empty(self):
        return True if self._queue is None else False

    def size(self):
        print("Size of Queue is {}".format(len(self)))
        return len(self)

    def __len__(self):
        l = 0
        s = self._queue
        while s is not None:
            l += 1
            s = s.next_node
        return l

    def print(self):
        print("Length: {}".format(len(self)))
        ele = []
        s = self._queue
        while s is not None:
            ele.append(s.item)
            s = s.next_node
        print(" --> ".join([str(e) for e in ele]))


if __name__ == "__main__":
    s = Queue()
    # s.print()
    s.enqueue(20)
    s.print()
    s.enqueue("hello")
    s.print()
    s.enqueue("2")
    s.print()
    s.size()
    s.dequeue()
    s.print()
    s.dequeue()
    s.print()
    s.dequeue()
    s.print()
    # print(s.is_empty())
    s.dequeue()
    s.print()
    s.enqueue("2")
    s.print()
    s.dequeue()
    s.print()
