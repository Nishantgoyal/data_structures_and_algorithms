from eight_puzzle import EightPuzzle
from eight_puzzle_backtrack import EightPuzzle


def main():
    ep = EightPuzzle()
    ep.print_puzzle()
    ep.solve_puzzle()
    # while True:
    #     print("Please provide Input: (m: to move; X: to quit)")
    #     inp = input()
    #     if inp in ["X", "x"]:
    #         break
    #     if inp == "m":
    #         ep.make_move()


if __name__ == "__main__":
    main()
