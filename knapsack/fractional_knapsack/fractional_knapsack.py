from copy import deepcopy
import json


class Knapsack:
    def __init__(self, knapsack_weight, items):
        self.knapsack_weight = knapsack_weight
        self.items = items
        self.knapsack = []

    def create_fraction_arr(self):
        items_len = len(self.items)
        for index in range(items_len):
            item = self.items[index]
            item["F"] = item["V"] / item["W"]

    def add_item_to_knapsack(self, item_index):
        print("Adding item at index: {} to Knapsack".format(item_index))
        item = self.items[item_index]
        weight = item["W"]
        value = item["V"]
        fraction = 1
        is_fraction = False
        if weight > self.knapsack_weight:
            fraction = self.knapsack_weight / weight
            is_fraction = True

        self.items.remove(item)
        self.knapsack_weight -= weight * fraction

        return {
            "W": weight * fraction,
            "V": value * fraction,
            "Fraction": is_fraction
        }

    def choose_item(self):
        print("Choosing an item...")
        fraction_arr = [item["F"] for item in self.items]
        index_max = fraction_arr.index(max(fraction_arr))
        return self.add_item_to_knapsack(index_max)

    def fill_knapsack(self):
        print("Filling Knapsack")
        self.create_fraction_arr()
        while self.knapsack_weight > 0:
            if len(self.items) == 0:
                print("No items Left")
                break
            print("Remaining Weight: {}".format(self.knapsack_weight))
            print("Items to Choose from: {}".format(
                json.dumps(self.items, indent=2)))
            item = self.choose_item()
            self.knapsack.append(item)
        print("Knapsack: {}".format(json.dumps(self.knapsack, indent=2)))
        print("Total Value: {}".format(self.get_value_of_knapsack()))

    def get_value_of_knapsack(self):
        return sum([item["V"] for item in self.knapsack])


def test():
    test_cases = [
        {
            "knapsack_weight": 7,
            "items": [
                {"W": 4, "V": 20},
                {"W": 3, "V": 18},
                {"W": 2, "V": 14}
            ]
        }
    ]
    for test_case in test_cases:
        knapsack = Knapsack(test_case["knapsack_weight"], test_case["items"])
        knapsack.fill_knapsack()


if __name__ == "__main__":
    test()
