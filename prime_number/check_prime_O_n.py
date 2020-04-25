import sys

'''

    Input: Number `n`

    Output: Tells whether the number is prime or not

    Complexity: O(n)

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


def check_prime(N):
    '''
        - For a given number `n`
            - loop over all the numbers `i` from 2 to (n-1)
            - if `n` is divisible by `i`, it is not a prime
        - if `n` is not divisible by any such `i`, it is a prime number
    '''
    is_prime = True
    if N == 1:  # Handling Special Case of N == 1
        is_prime = False
    for i in range(2, N):
        if N % i == 0:
            is_prime = False
            break
    return is_prime


def main():
    N = get_input()
    is_prime = check_prime(N)
    if is_prime:
        print("Input: {} is Prime".format(N))
    else:
        print("Input: {} is not Prime".format(N))


if __name__ == "__main__":
    main()
