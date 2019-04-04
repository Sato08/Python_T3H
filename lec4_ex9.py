import random
def list_(numbers, n):
    result = []
    sub = []
    for number in numbers:
        sub.append(number)
        if len(sub) == n:
            result.append(tuple(sub))
            sub = []
    return result
numbers = [random.randint(0, 100) for _ in range(20)]
n = 3
list_(numbers, n)