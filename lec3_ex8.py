def min_Max(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return (min_num, max_num)

min_Max([1, 4, 2, 6, 7, 11])