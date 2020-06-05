import sys
from gcd import GCD


def calculate_GCD_of_Arr(arr):
    gcd = arr[0]
    for ele in arr[1:]:
        gcd = GCD(gcd, ele).gcd
    return gcd


def main():
    num_array = list(map(int, sys.argv[1].split(",")))
    gcd = calculate_GCD_of_Arr(num_array)
    print(gcd)


if __name__ == "__main__":
    main()
