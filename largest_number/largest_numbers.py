import copy
import time
import json
import sys
from random import randint

from permutations import Permutations


class LargestNumber:
    '''
        __init__
        find_largest_number
        get_largest_from_array
        compare_digits_at_index
        is_index_valid
        compare_digit_with_remaining_arr
        is_digit_greater_than_number
        compare
        brute_force_algo
    '''

    def __init__(self, arr=None):
        if arr is not None:
            self.arr = copy.deepcopy(arr)
        self.large_number = []
        self._cache = {}

    def find_largest_number(self):
        l = len(self.arr)
        for _ in range(l):
            self.get_largest_from_array()
        largest_number = int("".join([
            str(ele)
            for ele in self.large_number
        ]))
        return largest_number

    def get_largest_from_array(self):
        largest = None
        # print("\nGetting Largest for Arr: {}".format(self.arr))
        for i in range(len(self.arr)):
            if largest is None:
                largest = self.arr[i]
                continue
            encoding = "{}-{}".format(largest, self.arr[i])
            if encoding in self._cache:
                # print("Getting largest from cache for {}".format(encoding))
                largest = self._cache[encoding]
            else:
                largest = self.compare(largest, self.arr[i])
                message = "Storing: {} in cache with value: {}".format(
                    encoding, largest)
                # print(message)
                self._cache[encoding] = largest
            # print("Largest: {}".format(largest))
        self.arr.remove(largest)
        self.large_number.append(largest)

    def compare_digits_at_index(self, dig_1, dig_2, index_1, index_2):
        # 0: both equal
        # 1: dig 1 is greater
        # -1: dig 2 is greate
        # print("Comparing digits at index {} and {}".format(index_1, index_2))
        value1 = dig_1[index_1]
        value2 = dig_2[index_2]
        if int(value1) == int(value2):
            # print("Equal")
            return 0
        elif int(value1) < int(value2):
            # print("{} is greater than {}".format(dig_2, dig_1))
            return -1
        else:
            # print("{} is greater than {}".format(dig_1, dig_2))
            return 1

    def is_index_valid(self, index, arr):
        return index < len(arr)

    def is_digit_greater_than_number(self, ith_digit, number):
        # print("Comparing: {} with: {}".format(ith_digit, number))
        for digit in number:
            if int(digit) > ith_digit:
                return False
            elif int(digit) < ith_digit:
                return True
        return True

    def compare(self, number_1, number_2):
        # print("Comparing {} and {}".format(number_1, number_2))
        if number_1 == number_2:
            return number_1
        dig_1 = str(number_1)
        dig_2 = str(number_2)
        i = j = 0
        while True:
            if self.is_index_valid(i, dig_1) and self.is_index_valid(j, dig_2):
                compare_digits = self.compare_digits_at_index(
                    dig_1, dig_2, i, j)
                if compare_digits == 1:
                    return number_1
                elif compare_digits == -1:
                    return number_2
                else:
                    i += 1
                    j += 1
            else:
                if self.is_index_valid(i, dig_1):
                    ith_digit = int(dig_1[i])
                    if self.is_digit_greater_than_number(ith_digit, dig_1):
                        return number_1
                    else:
                        return number_2
                else:
                    jth_digit = int(dig_2[j])
                    if self.is_digit_greater_than_number(jth_digit, dig_2):
                        return number_2
                    else:
                        return number_1
