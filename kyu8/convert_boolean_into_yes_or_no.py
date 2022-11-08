def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(bool_to_word(True))
    print(bool_to_word(False))
