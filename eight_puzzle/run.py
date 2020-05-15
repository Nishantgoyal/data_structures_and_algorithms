from eight_puzzle import EightPuzzle


def main():
    ep = EightPuzzle()
    ep.print_puzzle()
    moves = ep.possible_moves()
    print(moves)


if __name__ == "__main__":
    main()
