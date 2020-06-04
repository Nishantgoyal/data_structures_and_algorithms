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

    def get_nth_fibbo_number(self, N):
        if N == 0:
            return self.a
        if N == 1:
            return self.b
        i = 2
        for fibbo_num in self.next():
            if i == N:
                return fibbo_num
            i += 1
