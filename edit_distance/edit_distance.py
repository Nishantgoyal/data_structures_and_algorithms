class EditDistance:
    def __init__(self, str_a, str_b):
        self.str_a = str_a
        self.str_b = str_b
        self._cache = {}

    def get_dist(self, i, j):
        if i < 0 or j < 0:
            return 0
        dists = []
        if self.str_a[i] == self.str_b[j]:
            if (i - 1 >= 0) and (j - 1 >= 0):
                dists.append(self._cache[i - 1][j - 1])
            else:
                dists.append(max(i, j, 0))
        else:
            if (i - 1 >= 0):
                dists.append(self._cache[i - 1][j] + 1)
            if (j - 1 >= 0):
                dists.append(self._cache[i][j - 1] + 1)
            if (i - 1 >= 0) and (j - 1 >= 0):
                dists.append(self._cache[i - 1][j - 1] + 1)
            else:
                dists.append(max(i + 1, j + 1, 1))
        return min(dists)

    def get_edit_dist(self):
        l_a = len(self.str_a)
        l_b = len(self.str_b)
        for i in range(l_a):
            for j in range(l_b):
                if i not in self._cache:
                    self._cache[i] = {}
                self._cache[i][j] = self.get_dist(i, j)
                print("i:{} j:{} dist: {} str_a: {} str_b: {}".format(
                    i, j, self._cache[i][j],
                    self.str_a[0:i+1], self.str_b[0:j+1])
                )
        return self._cache[l_a - 1][l_b - 1]
