from string import ascii_lowercase
words = ['python', 'patience', 'documents', 'students', 'homework', 'practice', 
         'success', 'english', 'university','congratulation']

result_words = []
for word in words:
  count_values = 0
  for char in word:
    count_value = ascii_lowercase.index(char) + 1
    count_values += count_value
    result_words.append([word,count_values])
    
print(result_words)