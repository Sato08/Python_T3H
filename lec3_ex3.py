def name_File(name):
    result = []
    for index in range(len(name) - 1, -1, -1):
        if name[index] == ".":
            result.append(name[index - 1:: -1])
            break
    return result[0][:: -1]

name_File("word.docs.txt")