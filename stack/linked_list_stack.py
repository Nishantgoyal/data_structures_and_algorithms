
class Stack:
    class _Node:
        def __init__(self, item):
            self.item = item
            self.next_node = None

    def __init__(self):
        self._stack = None

    def push(self, ele):
        n = self._Node(ele)
        if self._stack is None:
            self._stack = n
        else:
            temp = self._stack
            self._stack = n
            n.next_node = temp

    def pop(self):
        if self._stack is None:
            return None
        ele = self._stack.item
        self._stack = self._stack.next_node
        return ele

    def is_empty(self):
        return True if self._stack is None else False

    def size(self):
        return len(self)

    def __len__(self):
        l = 0
        s = self._stack
        while s is not None:
            l += 1
            s = s.next_node
        return l

    def print(self):
        print("Length: {}".format(len(self)))
        ele = []
        s = self._stack
        while s is not None:
            ele.append(s.item)
            s = s.next_node
        print(" --> ".join([str(e) for e in ele]))


if __name__ == "__main__":
    s = Stack()
    s.print()
    s.push(20)
    s.print()
    s.push("hello")
    s.print()
    s.push("2")
    s.print()
    print(s.size())
    print(len(s))
    print(s.pop())
    s.print()
    print(s.pop())
    s.print()
    print(s.pop())
    s.print()
    print(s.is_empty())
    print(s.pop())
    s.print()
    s.push("2")
    s.print()
    print(s.pop())
    s.print()
