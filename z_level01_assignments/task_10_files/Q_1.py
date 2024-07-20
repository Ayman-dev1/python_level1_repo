# Program to Read file and store numbers in a list and calculate sum & Avg
new_lines_list = []
with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\read_data_numbers.txt", 'r') as my_file_reference:
    lines_list = my_file_reference.readlines()
    avg = 0
    total = 0
    for item in lines_list:
        item = item.strip()  # to remove any spaces
        item = float(item)
        if item != '':
            new_lines_list.append(item)
        total = total + item
        avg = total / len(lines_list)

print('Numbers : ', new_lines_list)
print('Total Sum : ', total)
print('Average : ', avg)
