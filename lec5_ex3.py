def sum_Money(number):
    sum_ = 0
    if number <= 50:
        sum_ = number * 15000
    elif number > 50 and number <= 200:
        sum_ = 50 * 15000 + (number - 50) * 16500
    else:
        sum_ = 50 * 15000 + 150 * 16500 + (number - 200) * 20000
    return sum_
sum_Money(48)
