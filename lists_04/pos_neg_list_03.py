# program to count, sum positive and negative numbers in a list
my_list = [15, -16, 20, -3, 0, 20]

# for each loop
total_pos, total_neg, count_pos, count_neg, count_zeros = 0, 0, 0, 0, 0

for item in my_list:
    if item > 0:
        total_pos = total_pos + item
        count_pos = count_pos + 1
    elif item < 0:
        total_neg = total_neg + item
        count_neg = count_neg + 1
    else:
        count_zeros = count_zeros + 1

print('total positive = ', total_pos, 'count pos =', count_pos)
print('total negative = ', total_neg, 'count neg =', count_neg)
print('count zeros = ', count_zeros)
