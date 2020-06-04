class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        while True:
            c = self.a + self.b
            self.a = self.b
            self.b = c
            yield c
