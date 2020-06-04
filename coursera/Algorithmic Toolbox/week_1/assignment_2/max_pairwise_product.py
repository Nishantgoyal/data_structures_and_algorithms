from random import randint
import sys


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_v2(numbers):
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    return max_1 * max_2


def stress_test():
    while True:
        n = randint(2, 11)
        print("Executing test for N: {}".format(n))
        numbers = [randint(0, 100) for _ in range(n)]
        print("Finding pairwise product for array:\n{}".format(
            numbers))
        sol_1 = max_pairwise_product(numbers)
        sol_2 = max_pairwise_product_v2(numbers)
        if sol_1 != sol_2:
            print("Solutions do not match: Sol1: {} Sol2: {}".format(sol_1, sol_2))
            sys.exit()
        print("SUCCESS...\n")


def main():
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_v2(input_numbers))


if __name__ == '__main__':
    # stress_test()
    main()
