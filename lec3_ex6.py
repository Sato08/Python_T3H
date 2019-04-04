def sum_Numbers(number):
    sum_value = 0
    for num in str(number):
        sum_value += int(num)
    return sum_value
sum_Numbers(12345)