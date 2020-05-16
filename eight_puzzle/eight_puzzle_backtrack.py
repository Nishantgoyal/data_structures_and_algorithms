from random import randint, seed
from copy import deepcopy
import json


class EightPuzzle:
    def __init__(self):
        self._tab_size = 0
        self.size = 3
        self._state = []
        self._blank_pos = None
        self._print("Initialising Eight Puzzle Class")
        self.initialize_puzzle()
        self.dump_state()
        self._print("Initialisation Complete")

    def initialize_puzzle(self):
        self._tab_size += 1
        self._print("Initializing Puzzle")
        permutation = self.create_permutation()
        puzzle = self.create_2d_puzzle_from_permutaion(permutation)
        all_moves = {str(moves): 0 for moves in self.get_all_possible_moves()}
        self._state.append({
            "puzzle": puzzle, "moves": all_moves
        })
        self._tab_size -= 1

    def get_all_possible_moves(self):
        self._tab_size += 1
        self._print("Getting all possible moves in the puzzle")
        blank_x, blank_y = self._blank_pos
        all_pos_moves = []
        if blank_x - 1 >= 0:
            all_pos_moves.append([blank_x - 1, blank_y])
        if blank_x + 1 < self.size:
            all_pos_moves.append([blank_x + 1, blank_y])
        if blank_y - 1 >= 0:
            all_pos_moves.append([blank_x, blank_y - 1])
        if blank_y + 1 < self.size:
            all_pos_moves.append([blank_x, blank_y + 1])
        self._print("All Possible Moves are: {}".format(all_pos_moves))
        self._tab_size -= 1
        return all_pos_moves

    def create_permutation(self):
        self._tab_size += 1
        self._print("Creating Permutation")
        permutation = []
        while True:
            element = randint(0, 8)
            if element not in permutation:
                self._tab_size += 1
                self._print("Chosen Element: {}".format(element))
                permutation.append(element)
                self._tab_size -= 1
            if len(permutation) >= (self.size ** 2):
                break
        self._print("Permutaion: {}".format(permutation))
        self._tab_size -= 1
        return permutation

    def create_2d_puzzle_from_permutaion(self, permutation):
        self._tab_size += 1
        self._print("Creating 2D from permutation: {}".format(permutation))
        puzzle = []
        for i in range(self.size):
            self._tab_size += 1
            puzzle.append([])
            for j in range(self.size):
                self._tab_size += 1
                index = (i * self.size) + j
                puzzle[i].append(permutation[index])
                if permutation[index] == 0:
                    self._blank_pos = [i, j]
                self._tab_size -= 1
            self._tab_size -= 1
        self._print("Created 2D puzzle from permutation: {}".format(puzzle))
        self._tab_size -= 1
        return puzzle

    def _print(self, message):
        sep = "  "
        print(sep * self._tab_size + str(message))
        # pass

    def dump_state(self):
        data = deepcopy(self._state)
        data = [
            {
                "puzzle": str(ele["puzzle"]),
                "moves": ele["moves"]
            }
            for ele in data]
        fName = "{}_state.json".format(__name__.split(".")[0])
        with open(fName, "w") as f:
            json.dump(data, f, indent=2)
