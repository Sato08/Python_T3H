def find_Number():
    result = []
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                if (a * c + b == 10 * c):
                    result.append([a, b, c])
    print(result)
find_Number()