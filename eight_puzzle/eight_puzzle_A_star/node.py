from copy import deepcopy


class Node:
    def __init__(self, board, num_of_moves, previous_node=None):
        self.board = deepcopy(board)
        self.num_of_moves = num_of_moves
        self.previous_node = previous_node
