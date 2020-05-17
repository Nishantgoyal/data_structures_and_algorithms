from random import randint, seed
from copy import deepcopy
import json
import sys
import time


class EightPuzzle:
    def __init__(self):
        self._tab_size = 0
        self.size = 3
        self._states = []
        self._invalid_states = []
        self._blank_pos = None
        self.current_state = {}
        self._print("Initialising Eight Puzzle Class")
        self.initialize_puzzle()
        # self.dummy_data()
        self.dump_state()
        self._print("Initialisation Complete")

    # def dummy_data(self):
    #     self.current_state["puzzle"] = [
    #         [2, 4, 3],
    #         [1, 8, 5],
    #         [7, 0, 6]
    #     ]
    #     self.current_state["blank"] = self.get_blank_pos()
    #     all_moves = {str(moves): 0 for moves in self.get_all_possible_moves()}
    #     self.push_state(puzzle, all_moves)

    # def get_state(self):
    #     state = self._states[-1]
    #     return state

    def push_state(self, puzzle=None, valid_moves=None):
        if puzzle is None:
            puzzle = deepcopy(self.current_state["puzzle"])
        blank_pos = self.get_blank_pos(puzzle)
        if valid_moves is None:
            valid_moves = {
                str(moves): 0
                for moves in self.get_all_possible_moves(blank_pos)
            }
        self.current_state = deepcopy({
            "puzzle": deepcopy(puzzle),
            "moves": deepcopy(valid_moves),
            "blank": deepcopy(blank_pos)
        })
        self._states.append(deepcopy(self.current_state))

    def get_blank_pos(self, puzzle=None):
        self._tab_size += 1
        if puzzle is None:
            puzzle = deepcopy(self.current_state["puzzle"])
        self._print("Getting Blank Pos for puzzle: {}".format(puzzle))
        for i in range(self.size):
            for j in range(self.size):
                if puzzle[i][j] == 0:
                    blank_pos = [i, j]
        self._print("Blank Position is: {}".format(blank_pos))
        self._tab_size -= 1
        return blank_pos

    def initialize_puzzle(self):
        self._tab_size += 1
        self._print("Initializing Puzzle")
        permutation = self.create_permutation()
        puzzle = self.create_2d_puzzle_from_permutaion(permutation)
        self.push_state(puzzle)
        self._tab_size -= 1

    def get_all_possible_moves(self, blank_pos=None):
        if blank_pos is None:
            blank_pos = deepcopy(self.current_state["blank"])
        self._tab_size += 1
        self._print("Getting all possible moves in the puzzle")
        blank_x, blank_y = blank_pos
        all_pos_moves = []
        if blank_x - 1 >= 0:
            all_pos_moves.append([blank_x - 1, blank_y])
        if blank_x + 1 < self.size:
            all_pos_moves.append([blank_x + 1, blank_y])
        if blank_y - 1 >= 0:
            all_pos_moves.append([blank_x, blank_y - 1])
        if blank_y + 1 < self.size:
            all_pos_moves.append([blank_x, blank_y + 1])
        self._print("All Possible Moves for blank: {} are: {}".format(
            blank_pos, all_pos_moves))
        self._tab_size -= 1
        return all_pos_moves

    def dump_state(self):
        data = deepcopy(self._states)
        data = [
            {
                "puzzle": str(ele["puzzle"]),
                "moves": ele["moves"]
            }
            for ele in data]
        fName = "{}_state.json".format(__name__.split(".")[0])
        with open(fName, "w") as f:
            json.dump(data, f, indent=2)

    def solve(self):
        self._tab_size += 1
        self._print("Solving Puzzle...")
        while not self.is_solved():
            self._tab_size += 1
            inp = input("Press 'm' to move, 'b' to backtrack, "
                        "'p' to print the current_state, any other key to quit\t")
            if inp == "m":
                valid_move = self.move()
                if not valid_move:
                    print("No Moves Present, BackTracking...")
                else:
                    print("Moving...")
            # time.sleep(0.05)
            # print(len(self._state))
            else:
                break
            self._tab_size -= 1
        else:
            print("Puzzle Solved")
        self._tab_size -= 1

    def move(self):
        self._tab_size += 1
        self._print("Making a Move")
        self.current_state = self._states.pop()
        self._print("Current State: {}".format(self.current_state))
        chosen_move = None
        for move in self.current_state["moves"]:
            if self.current_state["moves"][move] == 0:
                chosen_move = move
                break

        if chosen_move is not None:
            self._print("Chosen Move: {}".format(chosen_move))
            self.current_state["moves"][chosen_move] = 1
            self.push_state(
                self.current_state["puzzle"], self.current_state["moves"])
            # self._state.append(current_state)
            # self._print("Current State: {}".format(self._states))

            # puzzle = deepcopy(self.current_state["puzzle"])
            self._print("Current Puzzle: {}".format(
                self.current_state["puzzle"]))
            self._print("Blank before Move: {}".format(
                self.current_state["blank"]))

            self.make_move(self.current_state["puzzle"], chosen_move)

            self._print("Puzzle After Move: {}".format(
                self.current_state["puzzle"]))
            self._print("Blank After Move: {}".format(
                self.current_state["blank"]))

            # possible_moves = self.get_moves_from_state(puzzle)
            # self._print("Possible Moves for puzzle: {} are: {}".format(
            #     puzzle, possible_moves))
            if str(self.current_state["puzzle"]) not in self._invalid_states:
                self.push_state()
                # self._state.append({
                #     "puzzle": deepcopy(puzzle), "moves": deepcopy(possible_moves)
                # })
            else:
                print("Invalid..." + str(self.current_state["puzzle"]))
                # current_state = self._state[-1]["puzzle"]
                # for i in range(self.size):
                #     for j in range(self.size):
                #         if current_state[i][j] == 0:
                #             self._blank_pos = [i, j]
        else:
            self._invalid_states.append(str(self.current_state["puzzle"]))
        self._tab_size -= 1
        self.dump_state()
        return chosen_move is not None

    # def get_moves_from_state(self, cur_puzzle):
    #     self._tab_size += 1
    #     for state in self._state[::-1]:
    #         puzzle = state["puzzle"]
    #         if self.match_puzzle(cur_puzzle, puzzle):
    #             self._print("Puzzle Match. Possible moves for puzzle: {} are: {}".format(
    #                 puzzle, state["moves"]))
    #             return deepcopy(state["moves"])
    #     possible_moves = self.get_all_possible_moves()
    #     self._tab_size -= 1
    #     return {str(move): 0 for move in possible_moves}

    def make_move(self, puzzle, move):
        move_x, move_y = move.split(", ")
        move_x = int(move_x.strip().split("[")[1])
        move_y = int(move_y.strip().split("]")[0])

        blank_x, blank_y = self.current_state["blank"]
        puzzle[move_x][move_y], puzzle[blank_x][blank_y] = puzzle[blank_x][blank_y], puzzle[move_x][move_y]

    # def match_puzzle(self, puz1, puz2):
    #     match = True
    #     for i in range(self.size):
    #         for j in range(self.size):
    #             if puz1[i][j] != puz2[i][j]:
    #                 match = False
    #     return match

    def create_permutation(self):
        self._tab_size += 1
        self._print("Creating Permutation")
        permutation = []
        # seed(10)
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

    def is_solved(self):
        puzzle = self._states[-1]["puzzle"]
        for i in range(self.size):
            for j in range(self.size):
                req_value = ((i * self.size) + j + 1) % (self.size ** 2)
                val = puzzle[i][j]
                if val != req_value:
                    return False
        return True
