from random import randint

from edit_distance import EditDistance


def gen_random_string():
    n = randint(5, 10)
    string_arr = []
    for _ in range(n):
        string_arr.append(chr(randint(ord("a"), ord("b"))))
    return "".join(string_arr)


def main():
    while True:
        string_a = gen_random_string()
        string_b = gen_random_string()
        string_a = "bread"
        string_b = "really"
        print("String 1: {}\tString 2:{}".format(string_a, string_b))
        edit_distance = EditDistance(string_a, string_b)
        ed = edit_distance.get_edit_dist()
        print("Edit Dist: {}".format(ed))
        break


if __name__ == "__main__":
    main()
