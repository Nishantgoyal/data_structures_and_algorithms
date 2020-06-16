from random import randint

from red_black_tree import Tree


def test():
    n = 1
    arr = [randint(1, 10) for _ in range(n)]
    tree = Tree()
    print("Arr: {}".format(arr))
    for ele in arr:
        tree.insert(ele)


if __name__ == "__main__":
    test()
