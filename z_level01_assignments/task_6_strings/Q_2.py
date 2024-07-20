# program to capitalize the first and last letters of each word in a given string.

string = 'python exercise practice solution'

string = string.title()[::-1]
string_list = string.split()

for i in range(len(string_list)):
    string_list[i] = string_list[i][0].upper() + string_list[i][1:]
    string_list[i] = string_list[i][::-1]
print(' '.join(string_list))
