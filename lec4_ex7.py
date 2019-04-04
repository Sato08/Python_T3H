def is_Prime(number):
    count = 0
    for num in range(1, number):
        if number % num == 0:
            count += 1
    return count == 2

result = []
prime_num = 1
while (prime_num < 1000):
    if is_Prime(prime_num):
        result.append(prime_num)
    prime_num += 1
print(result)