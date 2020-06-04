from fibonacci import Fibonacci
import time


def print_fibonacci_numbers():
    fibbo = Fibonacci()
    # print(fibbo.a)
    print(fibbo.b)
    for ele in fibbo.next():
        print(ele)
        time.sleep(1)


def main():
    print_fibonacci_numbers()


if __name__ == "__main__":
    main()
