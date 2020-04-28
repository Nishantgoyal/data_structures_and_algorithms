class Node:
    item = ""
    next_node = None


class Stack:
    def __init__(self):
        self._stack = None

    def push(self, ele):
        n = Node()
        n.item = ele
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
            s = self._stack.next_node


if __name__ == "__main__":
    s = Stack()
    s.push(20)
    s.push("hello")
    s.push("2")
    print(s.size())
    print(len(s))
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())
    print(s.pop())
