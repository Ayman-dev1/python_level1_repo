# program to read from a file and write the content to another file

with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\read_data.txt", 'r') as my_file_reference:
    content = my_file_reference.read()

with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\write_data.txt", 'w') as my_file_reference:
    my_file_reference.write(content)
