from random import randint


class EightPuzzle:
    def __init__(self):
        self._n = 3
        self._puzzle = self.initialise_puzzle()

    def initialise_puzzle(self):
        puzzle = []
        while True:
            ele = randint(0, 8)
            # print("Choosen Element: {}".format(ele))
            if ele not in puzzle:
                puzzle.append(ele)
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
