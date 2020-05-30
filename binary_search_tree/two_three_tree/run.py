from two_three_tree import TwoThreeTree


def main():
    tree = TwoThreeTree()
    while True:
        print("\nPlease enter an Integer to Insert. Press 'X' to exit")
        inp = input()
        key = int(inp)
        tree.insert(key)
        tree.print_tree()


if __name__ == "__main__":
    main()