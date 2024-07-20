# program to count occurrences of a word in string

string = 'A computer science portal for portal'
word = 'portal'
num_of_repeated_words = 0

words_list = string.split()

for item in words_list:
    if item == word:
        num_of_repeated_words = num_of_repeated_words + 1

print(num_of_repeated_words)
