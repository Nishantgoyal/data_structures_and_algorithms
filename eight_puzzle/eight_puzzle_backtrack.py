from random import randint, seed
from copy import deepcopy
import json


class EightPuzzle:
    def __init__(self):
        self._tab_size = 0
        self.size = 3
        self._print("Initialising Eight Puzzle Class")
        self.initialize_puzzle()

    def initialize_puzzle(self):
        self._tab_size += 1
        self._print("Initializing Puzzle")
        permutation = self.create_permutation()
        self._tab_size -= 1

    def create_permutation(self):
        self._tab_size += 1
        self._print("Creating Permutation")
        permutation = []
        while True:
            element = randint(0, 8)
            if element not in permutation:
                self._tab_size += 1
                # self._print("Chosen Element: {}".format(element))
                permutation.append(element)
                self._tab_size -= 1
            if len(permutation) >= (self.size ** 2):
                break
        self._print("Permutaion: {}".format(permutation))
        self._tab_size -= 1
        return permutation

    def _print(self, message):
        sep = "  "
        print(sep * self._tab_size + str(message))
        # pass
