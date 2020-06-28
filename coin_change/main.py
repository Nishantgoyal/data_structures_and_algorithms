from random import randint
import time

# from greedy_change import Change
# from recursive_change import Change
from dynamic_change import Change


def main():
    # denominations = [1, 8, 20]
    denominations = [1, 2, 5, 7, 10, 15]
    change_class = Change(denominations)

    while True:
        amount = randint(1, 100)
        # amount = 32
        # print(amount)
        # amount = 10
        change = change_class.get_change(amount)
        # change_class.get_change(amount)
        print("Amount: {}\tChange: {}".format(amount, change))
        time.sleep(1)
        # break


if __name__ == "__main__":
    main()
