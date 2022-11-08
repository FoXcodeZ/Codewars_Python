def positive_sum(arr):
    sum_of_positive_numbers = 0
    if len(arr) > 0:
        for item in arr:
            if item > 0:
                sum_of_positive_numbers += item
        return sum_of_positive_numbers
    return 0


if __name__ == '__main__':
    array = [5, 4, -7, 5, -12, 9]   # We have to sum positive numbers ONLY, so we can't add -7 and -12.
    # 5 + 4 + 5 + 9 = 23
    print(positive_sum(array))
