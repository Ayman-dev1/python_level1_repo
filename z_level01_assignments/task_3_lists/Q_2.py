num_list = [23, 65, 19, 90]
size = len(num_list)

print("The Original List = ", num_list)
pos1, pos2 = 1, 3
temp = num_list[pos1]
num_list[pos1] = num_list[pos2]
num_list[pos2] = temp

print('After Swppping = ', num_list)