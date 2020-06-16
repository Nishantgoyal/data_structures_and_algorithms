from random import randint
import time

from greedy_change import Change


def main():
    denominations = [1, 2, 5, 10]
    change_class = Change(denominations)

    while True:
        amount = randint(1, 100)
        change = change_class.get_change(amount)
        print("Amount: {}\tChange: {}".format(amount, change))
        time.sleep(1)


if __name__ == "__main__":
    main()
