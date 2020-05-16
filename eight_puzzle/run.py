from eight_puzzle import EightPuzzle


def main():
    ep = EightPuzzle()

    ep.print_puzzle()

    ep.calculate_move_weight(None)
    # moves = ep.possible_moves()
    # ep.show_possible_moves(moves)
    # ep.show_blank_space()


if __name__ == "__main__":
    main()
