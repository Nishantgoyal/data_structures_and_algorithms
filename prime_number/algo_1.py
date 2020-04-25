import sys

'''

    The solution is written in O(n) complexity. 

    Input: Number `n`

    Algorithm:
    - For a given number `n`
      - loop over all the numbers `i` from 2 to (n-1)
      - if `n` is divisible by `i`, it is not a prime
    - if `n` is not divisible by any such `i`, it is a prime number

'''


def get_input():
    '''
        Gets the input from the command line argument. 
        Also checks if the input is a number.
        Throws an error if no command line argument is present
    '''
    if len(sys.argv) > 2:
        raise Exception("Extra Arguments Provided...!!!")
    elif len(sys.argv) == 1:
        raise Exception("Arguments not provided...!!!")
    return int(sys.argv[1])


def main():
    N = get_input()
    print("Input: {}".format(N))


if __name__ == "__main__":
    main()
