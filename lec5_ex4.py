import string
def max_Appear(document):
    for funt in string.punctuation:
        document = document.replace(funt, "")
    result = {}
    document = document.lower()
    for word in document.split():
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return sorted(result.items(), key = lambda x: x[1], reverse=True)[:10]
document = '''Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
'''
max_Appear(document)