import math


def find_short(s):
    words = s.split()  # We made a list of the words from give strings. Now we can iterate on this.
    shortest_word_length = math.inf  # Set to infinity, so we can use any length of word.

    for word in words:
        if len(word) < shortest_word_length:
            shortest_word_length = len(word)
    return shortest_word_length


if __name__ == '__main__':
    # Get the length of the shortest word in a sentence.
    print(find_short("Get over here"))
    print(find_short("Stop right there, criminal scum!"))
    print(find_short("May the Force be with you."))
    print(find_short("I'll be back"))
    print(find_short("Take your stinking paws off me, you damned dirty ape."))
    print(find_short("Here's Johnny!"))
