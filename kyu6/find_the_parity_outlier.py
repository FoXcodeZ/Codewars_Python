def find_outlier(integers):
    odd_list = [number for number in integers if number % 2 == 0]
    even_list = [number for number in integers if number % 2 != 0]
    if len(even_list) > len(odd_list):
        return odd_list[0]
    return even_list[0]


if __name__ == '__main__':
    list_a = [2, 4, 0, 100, 4, 11, 2602, 36]
    list_b = [160, 3, 1719, 19, 11, 13, -21]

    print(find_outlier(list_a))
    print(find_outlier(list_b))
