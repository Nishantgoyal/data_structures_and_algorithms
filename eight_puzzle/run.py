from eight_puzzle import EightPuzzle


def main():
    ep = EightPuzzle()

    ep.print_puzzle()
    ep.show_possible_moves()
    ep.show_blank_space()


if __name__ == "__main__":
    main()
