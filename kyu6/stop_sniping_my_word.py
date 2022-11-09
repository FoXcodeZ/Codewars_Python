def spin_words(sentence):
    if len(sentence.split()) == 1:
        if len(sentence) >= 5:
            return sentence[::-1]
        else:
            return sentence
    else:
        words = sentence.split()
        corrected_sentence = str()
        for word in words:
            if len(word) >= 5:
                corrected_sentence += word[::-1] + ' '
            else:
                corrected_sentence += word + ' '
        return corrected_sentence[:-1:]


if __name__ == '__main__':
    # Spin words, which have a length of 5 or more.
    # Add spaces only, when more than 1 word is presented.
    print(spin_words("Hey fellow warriors"))
    print(spin_words("This is a test"))
    print(spin_words("This is another test"))
    print(spin_words("Arachnophobia is a fear of spiders"))
    print(spin_words("Electrostatic"))
