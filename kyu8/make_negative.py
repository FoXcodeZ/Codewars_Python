def make_negative(number):
    return -abs(number)


if __name__ == '__main__':
    # We have to get negative numbers only.
    print(make_negative(-718))      # Should be -718
    print(make_negative(123))       # Should be -123
