import math


def is_square(n):
    if n >= 0:
        sqrt_n = int(math.sqrt(n))      # Get a square integer of provided number.
        return (sqrt_n * sqrt_n) == n   # Check if a number is a square number, and return a boolean value.
    return False


if __name__ == '__main__':
    # Check if a number is a perfect square number: https://en.wikipedia.org/wiki/Square_number
    print(is_square(-1))
    print(is_square(0))
    print(is_square(3))
    print(is_square(4))
    print(is_square(25))
    print(is_square(26))
    print(is_square(64))
    print(is_square(32))
    print(is_square(51))
