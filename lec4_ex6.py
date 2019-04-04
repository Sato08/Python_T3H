def fibonanci(num):
    if num == 0 or num == 1:
        fib = 1
    else:
        fib = fibonanci(num - 1) + fibonanci(num - 2)
    
    return fib
num = 0
result = []
while fibonanci(num) < 1000:
    result.append(fibonanci(num))
    num += 1
print(result)