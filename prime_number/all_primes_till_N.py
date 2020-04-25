import sys

import check_prime_O_n as prime_checker

'''

    Input: Number `n`

    Output: Prints the sequence of all numbers till N which are prime

'''


def get_input():
    '''
        Gets the input from the command line argument. 
        Throws an error if no or extra command line argument is present
    '''
    if len(sys.argv) > 2:
        raise Exception("Extra Arguments Provided...!!!")
    elif len(sys.argv) == 1:
        raise Exception("Arguments not provided...!!!")
    return int(sys.argv[1])


def main():
    N = get_input()
    prime_number_list = []
    for n in range(1, N + 1):
        is_prime = prime_checker.check_prime(n)
        if is_prime:
            prime_number_list.append(n)
    print("List of Primes: \n{}".format(
        ",".join([str(x) for x in prime_number_list])))


if __name__ == "__main__":
    main()
