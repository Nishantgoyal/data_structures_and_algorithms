import copy
import time
import json
import sys
from random import randint

from permutations import Permutations


class LargestNumberBrute:

    def __init__(self, arr=None):
        if arr is not None:
            self.arr = copy.deepcopy(arr)

    def find_largest_number(self):
        permutation_class = Permutations()
        all_perms = permutation_class.get_all_permutations(self.arr)
        max_number = None
        for perm in all_perms:
            get_number = int("".join([str(num) for num in perm]))
            if max_number is None:
                max_number = get_number
            else:
                if max_number < get_number:
                    max_number = get_number
            # print(get_number)
        return max_number
