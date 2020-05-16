from random import randint


class EightPuzzle:
    def __init__(self):
        self._n = 3
        self._blank_pos = None
        self._puzzle = self.initialise_puzzle()
        # self._puzzle = [[2, 8, 5],
        #                 [3, 4, 1],
        #                 [7, 6, 0]]
        # self._blank_pos = (2, 2)

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

    def show_blank_space(self):
        if self._blank_pos is not None:
            print("Blank Square at: {} {}".format(
                self._blank_pos[0], self._blank_pos[1]))
        else:
            print("Puzzle Not Initialised...")

    def show_possible_moves(self, moves):
        print("Possible Moves: {}".format(moves))

    def get_value_at_pos(self, x, y):
        return (
            x * self._n + y + 1
        )

    def get_difference(self, move, required_value_at_blank):
        move_x, move_y = move
        # value_at_move = self._puzzle[move_x][move_y]
        # # value_at_move = self._puzzle[move_x][move_y] - \
        # #     self.get_value_at_pos(move_x, move_y)
        # difference = value_at_move - required_value_at_blank
        # # difference = value_at_move
        '''
        Algo 1:
            val_at_pos_blank -> x
            val_at_pos_move -> y1
            val_at_move -> y2
            diff_at_pos_move -> abs(y2 - y1)
            diff -> abs(x - diff_at_pos_move)
        '''
        val_at_pos_blank = required_value_at_blank
        val_at_pos_move = self.get_value_at_pos(move_x, move_y)
        val_at_move = self._puzzle[move_x][move_y]
        diff_at_pos_move = abs(val_at_move - val_at_pos_move)
        difference = abs(val_at_pos_blank - diff_at_pos_move)
        print("Value at move:{} is {} and Difference is: {}".format(
            move, diff_at_pos_move, difference))
        return difference

    def get_max_move(self):
        print("Calculating Weight of Move")
        blank_x, blank_y = self._blank_pos
        required_value_at_blank = self.get_value_at_pos(blank_x, blank_y)
        print("Required Value at Blank: {} is {}".format(
            self._blank_pos, required_value_at_blank))
        moves = self.possible_moves()
        self.show_possible_moves(moves)
        max_move = None
        max_diff = -1
        for move in moves:
            difference = self.get_difference(move, required_value_at_blank)
            if max_move is None or difference > max_diff:
                max_move = move
                max_diff = difference
        print("Choosen Move: {}".format(max_move))
        return max_move

    def make_move(self):
        min_move_x, min_move_y = self.get_max_move()
        blank_x, blank_y = self._blank_pos
        weight_at_min_move = self._puzzle[min_move_x][min_move_y]

        self._puzzle[min_move_x][min_move_y] = 0
        self._puzzle[blank_x][blank_y] = weight_at_min_move

        self._blank_pos = (min_move_x, min_move_y)

        self.print_puzzle()
