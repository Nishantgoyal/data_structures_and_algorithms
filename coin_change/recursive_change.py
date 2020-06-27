class Change:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)
        # self._cache = {}

    def get_change(self, amount):
        if amount == 0:
            return 0
        min_change = None
        for d in self.denominations:
            if d <= amount:
                change = 1 + self.get_change(amount - d)
                if min_change is None:
                    min_change = change
                else:
                    if min_change > change:
                        min_change = change
        return min_change
