def flatten_List(numbers):
    result = []
    
    while numbers:
        num = numbers.pop()
        if isinstance(num, list):
            numbers = numbers + num
        else:
            result.append(num)
    return result[:: -1]

numbers = [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]
flatten_List(numbers)
