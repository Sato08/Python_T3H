result = open("results.txt", "w")
for number in range(1, 30000001):
    if number % 15 == 0:
        result.write("FizzBuzz\n")
    elif number % 3 == 0:
        result.write("Buzz\n")
    elif number % 5 == 0:
        result.write("Fizz\n")
    else:
        result.write(str(number) + "\n")
result.close()
