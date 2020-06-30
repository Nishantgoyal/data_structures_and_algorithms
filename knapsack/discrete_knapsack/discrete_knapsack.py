from copy import deepcopy
import json


class Knapsack:
    def __init__(self, knapsack_weight, items):
        self.knapsack_weight = knapsack_weight
        self.items = items
        self.knapsack = {}

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

    def choose(self, weight):
        print("Choosing Items")
        items = []
        for item in self.items:
            remaining_weight = weight - item["W"]
            items_in_knapsack = []
            if remaining_weight > 0:
                items_in_knapsack = self.knapsack[str(remaining_weight)]
            if item not in items_in_knapsack and item["W"] <= weight:
                items.append(item)
        print("Choosen Items: {}".format(items))
        return items

    def get_max_value_item(self, items, weight):
        print("Getting Max item to pick")
        choosen_item = None
        choosen_item_val = None
        for item in items:
            remaining_weight = weight - item["W"]
            remaining_weight_val = 0
            if remaining_weight > 0:
                remaining_weight_val = sum(
                    [i["V"] for i in self.knapsack[str(remaining_weight)]])
            value = item["V"] + remaining_weight_val
            if choosen_item is None:
                choosen_item = item
                choosen_item_val = value
            else:
                if value > choosen_item_val:
                    choosen_item = item
                    choosen_item_val = value
        print("Max item picked: {}".format(choosen_item))
        return choosen_item

    def choose_item(self, weight):
        print("Choosing Max item for weight...{}".format(weight))
        if weight <= 0:
            return []
        items = self.choose(weight)
        choosen_item = self.get_max_value_item(items, weight)
        remaining_weight = weight
        if choosen_item is not None:
            remaining_weight = weight - choosen_item["W"]
        print("Remaining Weight: {}".format(remaining_weight))
        if remaining_weight == weight:
            return self.knapsack[str(weight - 1)]
        else:
            remaining_weight_items = []
            if remaining_weight > 0:
                remaining_weight_items = self.knapsack[str(remaining_weight)]
            return remaining_weight_items + [choosen_item]

    def fill_knapsack(self):
        print("Filling Knapsack")
        print("Required Weight: {}".format(self.knapsack_weight))
        print("All Items: {}".format(self.items))
        for i in range(self.knapsack_weight + 1):
            self.knapsack[str(i)] = self.choose_item(i)
            print("Knapsack: {}".format(json.dumps(self.knapsack)))

        with open("{}.json".format(__file__.split(".")[0]), "w") as f:
            json.dump(self.knapsack, f, indent=2)

    def get_value_of_knapsack(self):
        return sum([item["V"] for item in self.knapsack])


def test():
    test_cases = [
        {
            "knapsack_weight": 15,
            # "knapsack_weight": 7,
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
