import copy
import time
import json
import sys
from random import randint


class LargestNumber:
    def __init__(self, arr=None):
        if arr is not None:
            self.arr = copy.deepcopy(arr)
        self.large_number = []

    def find_largest_number(self):
        l = len(self.arr)
        for _ in range(l):
            self.get_largest()

    def get_largest(self):
        largest = None
        print("Getting Largest from Arr: {}".format(self.arr))
        for i in range(len(self.arr)):
            print("Comparing: {}".format(self.arr[i]))
            if largest is None:
                largest = self.arr[i]
                continue
            largest = self.compare(largest, self.arr[i])
            print("Largest: {}".format(largest))
        self.arr.remove(largest)
        self.large_number.append(largest)

    def compare_digits_at_index(self, dig_1, dig_2, index_1, index_2):
        # 0: both equal
        # 1: dig 1 is greater
        # -1: dig 2 is greate
        print("Comparing digits at index {} and {}".format(index_1, index_2))
        value1 = dig_1[index_1]
        value2 = dig_2[index_2]
        if int(value1) == int(value2):
            print("Equal")
            return 0
        elif int(value1) < int(value2):
            print("{} is greater than {}".format(dig_2, dig_1))
            return -1
        else:
            print("{} is greater than {}".format(dig_1, dig_2))
            return 1

    def is_index_valid(self, index, arr):
        return index < len(arr)

    def compare_digit_with_remaining_arr(self, i, dig_1):
        digit = int(dig_1[i])
        all_remaining_digits = [
            int(str(ele)[0])
            for ele in self.arr
        ]
        max_remaining_digit = max(all_remaining_digits)
        if max_remaining_digit >= digit:
            return False
        else:
            return True

    def compare(self, number_1, number_2):
        print("Comparing {} and {}".format(number_1, number_2))
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
                    if self.compare_digit_with_remaining_arr(i, dig_1):
                        return number_1
                    else:
                        return number_2
                else:
                    if self.compare_digit_with_remaining_arr(j, dig_2):
                        return number_2
                    else:
                        return number_1
            # if int(dig_1[i]) == int(dig_2[j]):
            #     increment = False
            #     if i < len(dig_1) - 1:
            #         i += 1
            #         increment = True
            #     if j < len(dig_2) - 1:
            #         j += 1
            #         increment = True
            #     if not increment:
            #         return number_1
            # elif int(dig_1[i]) > int(dig_2[j]):
            #     return number_1
            # else:
            #     return number_2

    def brute_force_algo(self):
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

    def get_arr(self):
        arr_size = randint(2, 10)
        ele_upper_bound = 200
        arr = [
            randint(2, ele_upper_bound)
            for _ in range(arr_size)
        ]
        return arr

    def test(self):
        # self.arr = self.get_arr()
        self.arr = [124, 118, 16, 165, 181, 182, 43, 18, 55, 112]
        print("Array: {}".format(self.arr))

        # Brute Force
        # largest_number_brute = self.brute_force_algo()
        largest_number_brute = 55431821818116516124118112
        # print("Array: {}".format(arr))

        # # Original Algo
        # print("Array: {}".format(arr))
        self.find_largest_number()
        largest_number = int("".join([
            str(ele)
            for ele in self.large_number
        ]))

        if largest_number != largest_number_brute:
            print("Error: Largest Number Brute: {}, largest number algo: {}".format(
                largest_number_brute, largest_number))
            print(type(largest_number))
            print(type(largest_number_brute))
            sys.exit()
        print("Largest Number: {}".format(largest_number))


class Permutations:

    def get_all_permutations(self, arr):
        # print("Getting permutations for Array: {}".format(arr))
        if arr == []:
            return
        if len(arr) == 1:
            return [arr]
        ele = arr[0]
        # print("First Element is: {}".format(ele))
        # print("Obtaining Permutation for sub_array: {}".format(arr[1:]))
        sub_perm = self.get_all_permutations(arr[1:])
        # print("Permutations obtained for sub-array: {} are: {}".format(
        #     arr[1:], sub_perm))
        return self.merge_permutions(ele, sub_perm)

    def merge_permutions(self, ele, sub_perms):
        # print("Merging Ele: {} into Sub-Perm: {}".format(ele, sub_perms))
        permutations = []
        for sub_perm in sub_perms:
            for i in range(0, len(sub_perm)):
                new_perm = self.insert_num_into_array_at_index(
                    sub_perm, ele, i)
                permutations.append(new_perm)
            new_perm = self.insert_num_into_array_at_index(
                sub_perm, ele, len(sub_perm))
            permutations.append(new_perm)
        return permutations

    def insert_num_into_array_at_index(self, arr, ele, index):
        # print("Inserting Ele: {} into Array: {} at index: {}".format(
        #     ele, arr, index))
        arr_copy = copy.deepcopy(arr)
        new_arr = arr_copy[:index] + [ele] + arr_copy[index:]
        # print("\tNew Array: {}".format(new_arr))
        return new_arr

    def test(self):
        count = 3
        arr = list(range(1, count+1))
        permutations = [
            ",".join([
                str(ele)
                for ele in perm
            ])
            for perm in self.get_all_permutations(arr)
        ]
        print("Array: {}".format(arr))
        self.save_to_file(permutations)
        # permutations_json = json.dumps(permutations, indent=4)
        # print("Permutations: {}".format(permutations_json))

    def save_to_file(self, data):
        fN = "{}.json".format(__file__.split(".")[0])
        with open(fN, "w") as file_name:
            json.dump(data, file_name, indent=4)


def main():
    run_test()


def run_test():
    largest = LargestNumber()
    largest.test()
    # permutations = Permutations()
    # permutations.test()


def stress_test():
    while True:
        run_test()
        time.sleep(1)


if __name__ == "__main__":
    main()
    # stress_test()

'''
self.arr = [124, 118, 16, 165, , , , 18, , 112]
    55 43 182 181
BF: 55 43 182 18  181 16516124118112
    55 43 182 181 18  16516124118112
'''
