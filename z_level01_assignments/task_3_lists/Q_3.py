
my_list = [1, 6, 3, 5, 3, 4]
num = 4


is_found = False
indexes_list = []
for i in range(len(my_list)):
   if num == my_list[i]:
        indexes_list.append(i)
        is_found = True

if is_found:
    print('item is found on indexes : ', indexes_list)
else:
    print('item is not found')
