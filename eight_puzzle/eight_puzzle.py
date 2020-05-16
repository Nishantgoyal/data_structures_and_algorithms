from random import randint


class EightPuzzle:
    def __init__(self):
        self._n = 3
        self._blank_pos = None
        self._puzzle = self.initialise_puzzle()

    def initialise_puzzle(self):
        puzzle = []
        while True:
            ele = randint(0, 8)
            if ele not in puzzle:
                puzzle.append(ele)
                if ele == 0:
                    self._blank_pos = (
                        puzzle.index(0) // self._n,
                        puzzle.index(0) % self._n
                    )
            if len(puzzle) == self._n ** 2:
                break
        return self.convert_to_square(puzzle)

    def convert_to_square(self, puzzle):
        puzzle_square = []
        for i in range(self._n):
            puzzle_square.append([])
            for j in range(self._n):
                ind = i * self._n + j
                puzzle_square[i].append(puzzle[ind])
        return puzzle_square

    def print_puzzle(self):
        vertical_seperator = "---"
        for row in self._puzzle:
            print(vertical_seperator * self._n)
            print(" | ".join([str(ele) for ele in row]))
        print(vertical_seperator * self._n)

    def possible_moves(self):
        x, y = self._blank_pos
        moves = []
        if x - 1 >= 0 and y >= 0:
            moves.append((x - 1, y))
        if x + 1 >= 0 and y >= 0:
            moves.append((x + 1, y))
        if x >= 0 and y - 1 >= 0:
            moves.append((x, y - 1))
        if x >= 0 and y + 1 >= 0:
            moves.append((x, y + 1))
        return moves

    def show_blank_space(self):
        if self._blank_pos is not None:
            print("Blank Square at: {} {}".format(
                self._blank_pos[0], self._blank_pos[1]))
        else:
            print("Puzzle Not Initialised...")

    def show_possible_moves(self):
        moves = self.possible_moves()
        print("Possible Moves: {}".format(moves))
