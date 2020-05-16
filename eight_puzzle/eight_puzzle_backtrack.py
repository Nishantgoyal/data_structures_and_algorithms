from random import randint, seed
import copy


class EightPuzzle:
    def __init__(self):
        self._n = 3
        self._blank_pos = None
        self._puzzle = self.initialise_puzzle()
        self._track = []
        # self._puzzle = [[1, 2, 3],
        #                 [4, 5, 6],
        #                 [7, 8, 0]]
        # self._blank_pos = (2, 2)

    def initialise_puzzle(self):
        puzzle = []
        seed(2)
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

    def all_possible_moves(self):
        x, y = self._blank_pos
        self.show_blank_space()
        moves = []
        if x - 1 >= 0:
            moves.append((x - 1, y))
        if x + 1 < self._n:
            moves.append((x + 1, y))
        if y - 1 >= 0:
            moves.append((x, y - 1))
        if y + 1 < self._n:
            moves.append((x, y + 1))
        return moves

    def is_solved(self):
        for i in range(self._n):
            for j in range(self._n):
                required_val = self.get_value_at_pos(i, j)
                val = self._puzzle[i][j]
                # print("Req Val at ({},{}) is {}, Val is {}".format(
                #     i, j, required_val, val))
                if required_val != val:
                    return False
        return True

    def match_puzzle(self, puzzle):
        for i in range(self._n):
            for j in range(self._n):
                required_val = puzzle[i][j]
                val = self._puzzle[i][j]
                if required_val != val:
                    return False
        return True

    def make_move(self, move):
        move_x, move_y = move
        blank_x, blank_y = self._blank_pos
        weight_at_min_move = self._puzzle[move_x][move_y]

        self._puzzle[move_x][move_y] = 0
        self._puzzle[blank_x][blank_y] = weight_at_min_move

        self._blank_pos = (move_x, move_y)

        self.print_puzzle()

    def move(self):
        print("\tMaking a Move")

        all_moves = self.all_possible_moves()

        possible_moves = {move: True for move in all_moves}

        for state in self._track:
            puzzle = state["puzzle"]
            if self.match_puzzle(puzzle):
                moves = state["moves"]
                for move in moves:
                    if moves[move] == False:
                        possible_moves[move] = False
        print("Current Tracker: {}".format(self._track))

        is_move_possible = False
        chosen_move = None

        for move in possible_moves:
            if possible_moves[move]:
                is_move_possible = True
                chosen_move = move
        possible_moves[chosen_move] = False

        print("All Possible Moves: {}".format(possible_moves))
        print("Chosen Move: {}".format(chosen_move))
        if not is_move_possible:
            print("No Move Possible")
        else:
            state = {}
            state["puzzle"] = copy.deepcopy(self._puzzle)
            state["moves"] = copy.deepcopy(possible_moves)
            self._track.append(state)
            self.make_move(chosen_move)

    def solve_puzzle(self):
        print("Starting to Solve the puzzle...")
        print("\nInitial Puzzle")
        self.print_puzzle()
        while not self.is_solved():
            print("Press 'm' to make a move, any other key to quit")
            if input() == "m":
                self.move()
            else:
                break
        else:
            print("Solved")

    def print_puzzle(self):
        vertical_seperator = "---"
        for row in self._puzzle:
            print(vertical_seperator * self._n)
            print(" | ".join([str(ele) for ele in row]))
        print(vertical_seperator * self._n)

    def show_blank_space(self):
        if self._blank_pos is not None:
            print("Blank Square at: {} {}".format(
                self._blank_pos[0], self._blank_pos[1]))
        else:
            print("Puzzle Not Initialised...")

    def convert_to_square(self, puzzle):
        puzzle_square = []
        for i in range(self._n):
            puzzle_square.append([])
            for j in range(self._n):
                ind = i * self._n + j
                puzzle_square[i].append(puzzle[ind])
        return puzzle_square

    def get_value_at_pos(self, x, y):
        return (
            (x * self._n + y + 1) % (self._n ** 2)
        )
