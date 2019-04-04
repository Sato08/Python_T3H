def solve():
    first_half = []
    full_result = []
    for sum1 in range(5, 87):
        len1 = len([[a, e, d, f]
                    for a in range(1, 10)
                    for d in range(1, 10)
                    for e in range(1, 10)
                    for f in range(1, 10)
                    if a + d + 12 * e - f == sum1])

        if len1 > 0:
            first_half.append([sum1, len1])
    for sum1, len1 in first_half:
        len2 = len([[b, c, g, h, i]
                    for b in range(1, 10)
                    for c in range(1, 10)
                    for g in range(1, 10)
                    for h in range(1, 10)
                    for i in range(1, 10)
                    if c * i * sum1 + i * 13 * b + c * g * h 
                    == 87 * c * i])
        if len2 > 0:
            full_result.append([sum1, len1*len2])

    result = sum([i[1] for i in full_result])
    return result
solve()