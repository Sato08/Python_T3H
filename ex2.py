data = open("results.txt", "r")
count = 0
for _ in data.size():
    data.readline()
    count += 1
    if count > 30000000 - 9:
        print(data.readline())
data.close()
'''
'2999991\n'
'2999992\n'
'2999993\n'
'Buzz\n'
'Fizz\n'
'2999996\n'
'Buzz\n'
'2999998\n'
'2999999\n'
'FizzBuzz\n'
'''
