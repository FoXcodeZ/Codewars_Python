def to_csv_text(t_array):
    out_string = str()
    for column in t_array:
        for item in column:
            out_string += str(item) + ","   # Add the number as a string and a comma after the number.
        out_string = out_string[:-1:]       # Delete the last, additional comma in the line.
        out_string += "\n"                  # Add enter at the end of the line.
    out_string = out_string[:-1:]           # Delete the last additional enter sign in the string.
    return out_string


if __name__ == '__main__':
    array = [[0, 1, 2, 3, 4],
             [10, 11, 12, 13, 14],
             [20, 21, 22, 23, 24],
             [30, 31, 32, 33, 34]]

    print(to_csv_text(array))
