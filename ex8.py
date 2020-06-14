result = []
samples = ["python", None, "cpython", True, 1, 1 + 1j, False, [100, 200, 300], 99.99, (31, "January")]
for sample in samples:
  if (isinstance(sample, (int, float, complex)) and sample is not True and sample is not False):
    result.append(sample)
print(result)
''' [1, (1+1j), 99.99] '''