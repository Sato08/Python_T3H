def fizz_Buzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Buzz"
    elif number % 5 == 0:
        return "Fizz"
    else:
        return number

result = []
for num in range(1, 101):
    result.append(fizz_Buzz(num))
print(result)