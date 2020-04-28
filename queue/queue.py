class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, ele):
        print("Enqueuing element: {}".format(ele))
        self._queue.append(ele)

    def dequeue(self):
        ele = None
        if len(self._queue) > 0:
            ele = self._queue[0]
            del self._queue[0]
        print("Dequeued Element: {}".format(ele))
        return ele

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        print("Size of Queue is {}".format(len(self)))
        return len(self)

    def __len__(self):
        return len(self._queue)

    def print(self):
        print(self._queue)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(20)
    s.print()
    s.enqueue("hello")
    s.print()
    s.enqueue("2")
    s.print()
    s.size()
    # print(len(s))
    s.dequeue()
    s.print()
    s.dequeue()
    s.print()
    s.dequeue()
    s.print()
