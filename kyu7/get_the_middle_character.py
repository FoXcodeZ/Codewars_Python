def get_middle(s):
    start = (len(s) - 1) // 2   # Middle of the string.
    end = start                 # The same position if the string length is odd.
    if len(s) % 2 == 0:         # If string length is even number, then we gave to return 2 strings.
        end = len(s) // 2
    return s[start:end+1]       # Remember about CS numeration from zero, we have to add 1 to the end.


if __name__ == '__main__':
    # Get the middle of the word, 1 letter if the word length is odd, and 2 letters if the word length is even.
    print(get_middle("abrogation"))
    print(get_middle("Deoxyribonucleic"))
    print(get_middle("Hello"))
    print(get_middle("Hey"))
