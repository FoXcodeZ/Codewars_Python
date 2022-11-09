def digital_root(t_number):
    str_number = str(t_number)
    digits = []
    out_sum = 0

    if len(str_number) == 1:
        return int(t_number)

    while len(str_number) > 1:
        out_sum = 0
        for digit in str_number:
            digits.append(int(digit))
            out_sum += int(digit)
        str_number = str(out_sum)
    return out_sum


if __name__ == '__main__':
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
