count = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            for h in range(1, 10):
                                for i in range(1, 10):
                                    if((a + d - f - 11 -10) * c * i + 13 * b * i + g * h * c == 66 * c * i):
                                        count += count
    print(count)