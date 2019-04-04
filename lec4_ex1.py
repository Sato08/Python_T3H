def is_Palindrome(words):
    words = words.lower()
    return words == words[::-1]

is_Palindrome("abb")