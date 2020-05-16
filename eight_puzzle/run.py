from eight_puzzle import EightPuzzle


def main():
    ep = EightPuzzle()
    ep.print_puzzle()

    while True:
        print("Please provide Input: (m: to move; X: to quit)")
        inp = input()
        if inp == "X":
            break
        if inp == "m":
            ep.make_move()


if __name__ == "__main__":
    main()
