from two_three_tree import TwoThreeTree


def main():
    tree = TwoThreeTree()
    while True:
        print(
            "Please choose an operation to perform: {I - Insert}. Any other key to Exit...")
        inp = input()
        if inp == "I":
            print("Please input a Integer to insert..")
            key = int(input())
            tree.insert(key)
            tree.print_tree()
        else:
            break


if __name__ == "__main__":
    main()
