class Change:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)

    def get_change(self, amount):
        change = {}
        for denomination in self.denominations:
            # print(denomination, amount)
            if amount >= denomination:
                denomination_count = amount // denomination
                change[str(denomination)] = denomination_count
                amount = amount % denomination
        return change
