import math
import string


def high_and_low(numbers):
    # numbers is a string, so we need to change it.
    # We are going to change numbers into a list of strings, without any spaces.

    numbers = numbers.split()  # We split numbers into the list here and remove all the spaces.
    highest = -math.inf  # "highest" is negative infinity, so we can guarantee at least 1 number is higher than this.
    lowest = math.inf  # "lowest" is positive infinity, so we can guarantee at least 1 number is lower than this.

    for item in numbers:
        if int(item) > highest:  # We have to remember item is a string, so we convert it to int.
            highest = int(item)
        if int(item) < lowest:
            lowest = int(item)
    return f"{highest} {lowest}"


if __name__ == "__main__":
    string_of_numbers = "1 7 -3 6 5"        # Here 7 is the highest number, and -3 is the lowest number.
    print(high_and_low(string_of_numbers))
