num_list = [1, 6, 3, 6, 3, 6]
multiply_list = num_list.copy()


for i in range(len(num_list)):
    multiply_list[i] = multiply_list[i] * 2

print(' Original list =', num_list)
print('multiply list =', multiply_list)