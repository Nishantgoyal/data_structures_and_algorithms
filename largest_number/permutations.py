import copy
import time
import json
import sys
from random import randint


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
