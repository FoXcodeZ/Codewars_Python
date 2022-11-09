def validate_pin(pin):
    if pin.isdecimal() and (len(pin) == 4 or len(pin) == 6):
        return True
    return False


if __name__ == "__main__":
    # The PIN can be only 4 or 6 digits in length.
    # Only digits are allowed.
    print(validate_pin("1234"))
    print(validate_pin("12345"))
    print(validate_pin("a234"))
