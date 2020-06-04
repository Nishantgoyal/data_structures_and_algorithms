import json
import sys


class Tower:
    def __init__(self):
        self.N = int(sys.argv[1])
        self.tower = {}

    def initialise_tower(self, initial_rod):
        print("Initialising Tower...")
        self.tower["one"] = []
        self.tower["two"] = []
        self.tower["three"] = []
        if self.is_valid_rod(initial_rod):
            self.tower[initial_rod] = [ele for ele in range(self.N, 0, -1)]
        else:
            print("Invalid rod: {}".format(initial_rod))

    def print_tower(self):
        f_name = "{}.json".format(__file__.split(".")[0])
        with open(f_name, "w") as fN:
            json.dump(self.tower, fN, indent=4)
        print(json.dumps(self.tower, indent=4))

    def is_valid_rod(self, rod):
        return rod in ["one", "two", "three"]

    def is_rod_empty(self, rod):
        return len(self.tower[rod]) == 0

    def get_mid_rod(self, initial_rod, final_rod):
        for rod in ["one", "two", "three"]:
            if rod not in [initial_rod, final_rod]:
                return rod

    def move_a_piece(self, source_rod, destination_rod):
        if self.is_valid_rod(source_rod) and self.is_valid_rod(destination_rod):
            if self.is_rod_empty(source_rod):
                print("Source Rod: {} is empty")
            else:
                source_piece = self.tower[source_rod].pop()
                print("Moving Piece: {} from Source '{}' to Destination '{}'".format(
                    source_piece, source_rod, destination_rod))
                self.tower[destination_rod].append(source_piece)
        else:
            print("Source or destination is wrong")

    def is_solved(self, destination_rod):
        print("Checking is solved")
        blocks = self.tower[destination_rod]
        print("Blocks: {}".format(blocks))
        ini = self.N
        if len(blocks) != ini:
            return False
        for i in range(len(blocks)):
            if blocks[i] != ini:
                return False
            ini -= 1
        return True

    def solve(self, initial_rod, final_rod, N=None):
        if N is None:
            N = self.N
        if N == 0:
            return
        mid_rod = self.get_mid_rod(initial_rod, final_rod)      # three
        self.solve(initial_rod, mid_rod, N - 1)
        self.move_a_piece(initial_rod, final_rod)
        self.solve(mid_rod, final_rod, N - 1)
