import copy


class Change:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)
        self._cache = {}

    def change(self, amount):
        if amount in self._cache:
            return self._cache[amount]["change"]

        if amount == 0:
            self._cache[amount] = {}
            self._cache[amount]["change"] = 0
            self._cache[amount]["curr"] = {}
            return 0

        min_change = None
        curr = {}
        for d in self.denominations:
            if d <= amount:
                change = 1 + self.change(amount - d)
                if min_change is None:
                    min_change = change
                    curr = copy.deepcopy(self._cache[amount - d]["curr"])
                    if d not in curr:
                        curr[d] = 0
                    curr[d] += 1
                else:
                    if min_change > change:
                        min_change = change
                        curr = copy.deepcopy(self._cache[amount - d]["curr"])
                        if d not in curr:
                            curr[d] = 0
                        curr[d] += 1
        self._cache[amount] = {}
        self._cache[amount]["change"] = min_change
        self._cache[amount]["curr"] = copy.deepcopy(curr)
        return min_change

    def get_change(self, amount):
        # min_change = None
        for i in range(1, amount + 1):
            # print("Getting Change for: {}".format(i))
            self.change(i)
        return self._cache[amount]
