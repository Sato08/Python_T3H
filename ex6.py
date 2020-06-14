fib_1 = 1
fib_2 = 2
result = [1]
while(fib_2 < 1000):
	temp = fib_1
	fib_1 = fib_2
	fib_2 += temp
	result.append(fib_1)
print(result)
'''
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
'''