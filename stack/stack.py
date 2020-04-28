class Stack:
    def __init__(self):
        self._arr = []

    def push(self, ele):
        self._arr.append(ele)

    def pop(self):
        ele = None
        if len(self._arr) > 0:
            ele = self._arr[-1]
            del self._arr[-1]
        return ele


if __name__ == "__main__":
    s = Stack()
    s.push(20)
    s.push("hello")
    s.push("2")
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
