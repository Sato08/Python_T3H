from operator import itemgetter
import string
lines = open("python.txt", "r")
result = {}
for line in lines:
    line = line.lower()
    token = line.split(" ")

    for char in token:
        if(char in result.keys()):
            result.update({char : result[char] + 1})
        else:
            result.update({char : 1})
results = [(key, value) for key, value in result.items()]
results.sort(key = itemgetter(1),reverse = True)
print(results[:10])
print(dict(results[:10]))
'''
[('and', 20), ('the', 16), ('python', 15), ('to', 9), ('in', 6), ('of', 6), ('a', 5), ('for', 5), ('\n', 5), ('be', 5)]
{'and': 20, 'the': 16, 'python': 15, 'to': 9, 'in': 6, 'of': 6, 'a': 5, 'for': 5, '\n': 5, 'be': 5}
'''
