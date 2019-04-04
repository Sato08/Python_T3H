def sum_Inte(numbers):
    sum_num = 0
    int_num = 1
    for num in numbers:
        sum_num += num
        int_num *= num
    
    return (sum_num, int_num)

sum_Inte([2, 3, 4, 5, 6, 7, 8, 12])