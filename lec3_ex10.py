import string
def calculate_value(word):
    word = word.lower()
    result = 0
    for char in word:
        result += string.ascii_lowercase.index(char) + 1
    return result

calculate_value("Python")