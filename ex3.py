elc_numbers = [48, 100, 150, 199, 250, 1000]
for number in elc_numbers:
    sum_elc = 0;
    if number <= 50:
        sum_elc = number * 15000
        print("so dien:", number, "so tien: ", sum_elc)
    elif number > 50 and number <= 200:
        sum_elc = 50 * 15000 + (number - 50) * 16500
        print("so dien:", number, "so tien: ", sum_elc)
    else:
        sum_elc = 50 * 15000 + 150 * 16500 + (number - 200) * 20000
'''
so dien: 48 so tien:  720000
so dien: 100 so tien:  1575000
so dien: 150 so tien:  2400000
so dien: 199 so tien:  3208500
'''