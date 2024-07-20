numbers_list = [15, 16, 20, 3, 9, 20]

sum_even, count_even, sum_odd, count_odd = 0, 0, 0, 0
for item in numbers_list:
    if item % 2 == 0:
        sum_even = sum_even + item
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + item
        count_odd = count_odd + 1


print('sum even =', sum_even)
print('count even =', count_even)
print('sum odd =', sum_odd)
print('sum odd =', count_odd)