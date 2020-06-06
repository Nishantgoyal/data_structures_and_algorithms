import copy
import time
import json
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
        # print("Getting Largest from Arr: {}".format(self.arr))
        for i in range(len(self.arr)):
            # print("Comparing: {}".format(self.arr[i]))
            if largest is None:
                largest = self.arr[i]
                continue
            largest = self.compare(largest, self.arr[i])
            # print("Largest: {}".format(largest))
        self.arr.remove(largest)
        self.large_number.append(largest)

    def compare(self, number_1, number_2):
        # print("Comparing {} and {}".format(number_1, number_2))
        dig_1 = str(number_1)
        dig_2 = str(number_2)
        i = j = 0
        while True:
            # print("Comparing digits at index {} and {}".format(i, j))
            if int(dig_1[i]) == int(dig_2[j]):
                increment = False
                if i < len(dig_1) - 1:
                    i += 1
                    increment = True
                if j < len(dig_2) - 1:
                    j += 1
                    increment = True
                if not increment:
                    return number_1
            elif int(dig_1[i]) > int(dig_2[j]):
                return number_1
            else:
                return number_2

    def test(self):
        arr_size = randint(2, 5)
        ele_upper_bound = 20
        arr = [
            randint(2, ele_upper_bound)
            for _ in range(arr_size)
        ]
        print("Array: {}".format(arr))
        self.arr = arr
        self.find_largest_number()
        largest_number = "".join([
            str(ele)
            for ele in self.large_number
        ])
        print("Largest Number: {}".format(largest_number))


class Permutations:

    def get_all_permutations(self, arr):
        print("Getting permutations for Array: {}".format(arr))
        if arr == []:
            return
        if len(arr) == 1:
            return [arr]
        ele = arr[0]
        print("First Element is: {}".format(ele))
        print("Obtaining Permutation for sub_array: {}".format(arr[1:]))
        sub_perm = self.get_all_permutations(arr[1:])
        print("Permutations obtained for sub-array: {} are: {}".format(
            arr[1:], sub_perm))
        return self.merge_permutions(ele, sub_perm)

    def merge_permutions(self, ele, sub_perms):
        print("Merging Ele: {} into Sub-Perm: {}".format(ele, sub_perms))
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
        print("Inserting Ele: {} into Array: {} at index: {}".format(
            ele, arr, index))
        arr_copy = copy.deepcopy(arr)
        new_arr = arr_copy[:index] + [ele] + arr_copy[index:]
        print("\tNew Array: {}".format(new_arr))
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
    # largest = LargestNumber()
    # largest.test()
    permutations = Permutations()
    permutations.test()


def stress_test():
    while True:
        run_test()
        time.sleep(2)


if __name__ == "__main__":
    main()
    # stress_test()
