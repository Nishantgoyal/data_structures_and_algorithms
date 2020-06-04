from fibonacci import Fibonacci
import time


def print_fibonacci_numbers(fibbo):
    # print(fibbo.a)
    print(fibbo.b)
    for ele in fibbo.next():
        print(ele)
        time.sleep(1)


def main():
    fibbo = Fibonacci()
    # print_fibonacci_numbers(fibbo)
    N = 2
    nth_fibbo = fibbo.get_nth_fibbo_number(N)
    print("Fibbonacci number for {} is {}".format(
        N, nth_fibbo))


if __name__ == "__main__":
    main()
