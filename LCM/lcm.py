from random import randint
import time
import math
import copy


class LCM:
    def __init__(self, arr):
        self.arr = copy.deepcopy(arr)
        self.lcm = self.get_lcm()

    def check_if_arr_all_ones(self):
        return all(elem == 1 for elem in self.arr)

    def is_prime(self, N):
        """checks if given number is prime"""
        sqrt = int(math.sqrt(N)) + 1
        for i in range(2, sqrt):
            if N % i == 0:
                return False
        return True

    def next_prime_generator(self):
        """generates an infinite sequence of prime numbers"""
        N = 2
        while True:
            if self.is_prime(N):
                yield N
            N += 1

    def update_arr(self, divisor):
        """divides each element of the array by divisor, if it is divisible"""
        modified = False
        for index in range(len(self.arr)):
            if self.arr[index] % divisor == 0:
                self.arr[index] = self.arr[index] // divisor
                modified = True
        return modified

    def get_lcm(self):
        """
            Method to obtain the Least Common Multiplier for an array
            Args:
                Array
            Return:
                integer
        """
        lcm = 1
        divisor_gen = self.next_prime_generator()
        divisor = next(divisor_gen)
        while True:
            print("\nArray: {}".format(self.arr))
            print("Current Divisor: {}\tCurrent LCM: {}".format(divisor, lcm))
            if self.check_if_arr_all_ones():
                break
            value_modified = self.update_arr(divisor)
            if not value_modified:
                divisor = next(divisor_gen)
            else:
                lcm *= divisor
        return lcm


if __name__ == "__main__":
    arr = [randint(1, 11) for _ in range(5)]
    lcm = LCM(arr)
    print("\nFor Arr: {}\nLCM: {}".format(arr, lcm.lcm))
