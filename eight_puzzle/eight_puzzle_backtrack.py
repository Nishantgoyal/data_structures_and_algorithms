from random import randint, seed
from copy import deepcopy
import json


class EightPuzzle:
    def __init__(self):
        self._tab_size = 0
        self.size = 3
        self._print("Initialising Eight Puzzle Class")
        self.initialize_puzzle()
        self._print("Initialisation Complete")

    def initialize_puzzle(self):
        self._tab_size += 1
        self._print("Initializing Puzzle")
        permutation = self.create_permutation()
        self.create_2d_puzzle_from_permutaion(permutation)
        self._tab_size -= 1

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
                self._tab_size -= 1
            self._tab_size -= 1
        self._print("Created 2D puzzle from permutation: {}".format(puzzle))
        self._tab_size -= 1

    def _print(self, message):
        sep = "  "
        print(sep * self._tab_size + str(message))
        # pass
