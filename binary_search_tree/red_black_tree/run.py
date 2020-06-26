from random import randint

from red_black_tree import Tree, Node


def test():
    n = 10
    arr = [randint(1, 100) for _ in range(n)]
    tree = Tree()
    print("Arr: {}".format(arr))
    for ele in arr:
        tree.insert(ele)
        tree.print_tree()
    print("\nDone")
    print("Arr: {}".format(arr))
    tree.print_tree()


if __name__ == "__main__":
    test()
