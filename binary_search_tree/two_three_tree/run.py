from random import randint
import json

from two_three_tree import TwoThreeTree


def test():
    n = randint(10, 20)
    arr = [randint(1, 100) for _ in range(n)]
    arr = [80, 5, 7, 18, 84, 35, 59, 72, 48,
           79, 26, 56, 41, 35, 24, 21, 15, 27]
    print("Array: {}".format(arr))
    print("<<<<<<<<<<<<===============>>>>>>>>>>>>>")
    tree = TwoThreeTree()
    for ele in arr:
        print()
        tree.insert(ele)
    print("<<<<<<<<<<<<===============>>>>>>>>>>>>>")

    print(tree.get_tree())


def main():
    tree = TwoThreeTree()
    while True:
        print("\nPlease enter an Integer to Insert. Press 'X' to exit")
        inp = input()
        key = int(inp)
        tree.insert(key)
        tree.print_tree()


if __name__ == "__main__":
    test()
    # main()
