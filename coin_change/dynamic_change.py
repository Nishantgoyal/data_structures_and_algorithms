class Change:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)
        self._cache = {}

    def get_change(self, amount):
        # print("Getting Change for Amount: {}".format(amount))
        if amount in self._cache:
            return self._cache[amount]
        if amount == 0:
            return 0
        # min(get_change(amount - den) for all den)
        min_change = None
        choices = []
        for d in self.denominations:
            if d <= amount:
                change = 1 + self.get_change(amount - d)
                if min_change is None:
                    min_change = change
                else:
                    if min_change > change:
                        min_change = change
        self._cache[amount] = min_change
        return min_change
