def list_number(samples):
    result = []
    for sample in samples:
        if (isinstance(sample, (int, float, complex)) and sample is not True and sample is not False):
            result.append(sample)
    return result
samples = ["python", None, "cpython", True, 1, 1 + 1j, False, [100, 200, 300], 99.99, (31, "January")]
list_number(samples)