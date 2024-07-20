# lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# uniqueList = []
# duplicateList = []
# duplicated_many_times = []
#
# for item in lis:
#     if item not in uniqueList:
#         uniqueList.append(item)
#     elif item not in duplicateList:
#         duplicateList.append(item)
#     else:
#         duplicated_many_times.append(item)
#
# print(uniqueList)
# print(duplicateList)
# print(duplicated_many_times)



# newList = [12, 35, 9, 56, 89, 76]
# size = len(newList)
# # Swapping
# temp = newList[0]
# newList[0] = newList[size - 1]
# newList[size - 1] = temp
# print(newList)


new_list = [42, 65, 86, 76, 90]
size = len(new_list)
# swapping
temp = new_list[0]  # store new_list[0] in temp
new_list[0] = new_list[size - 1]  # new_list[0] == 90 or  the first item == the last item in list
new_list[size - 1] = temp  # the last item == first item

print(new_list)
