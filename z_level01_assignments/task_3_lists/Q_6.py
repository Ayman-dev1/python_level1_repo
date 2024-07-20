num_list = [23, 90, 19, 65]

max = num_list[0]
min = num_list[0]

for item in num_list:
    if item > max:
        max = item
    if item < min:
        min = item

print("Max number:", max)
print("Min number:", min)