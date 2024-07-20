num_list = [1, 6, 3, 6, 3, 6]
num = 6

count_occur = 0
for item in num_list:
    if item == num:
        count_occur = count_occur + 1

print('Number Appears in the list = ', count_occur, 'times')