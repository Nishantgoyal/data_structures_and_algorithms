from eight_puzzle import EightPuzzle
from eight_puzzle_backtrack import EightPuzzle


def main():
    ep = EightPuzzle()
    ep.solve()
    ep.dump_state()


if __name__ == "__main__":
    main()
