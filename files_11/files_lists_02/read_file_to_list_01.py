# program to read from text file and store in a list

new_lines_list = []
with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\countries.txt", 'r') as my_file_reference:
    lines_list = my_file_reference.readlines()
    print(lines_list)
    for item in lines_list:
        item = item.strip()  # to remove any spaces
        if item != '':
            new_lines_list.append(item)

print(new_lines_list)
