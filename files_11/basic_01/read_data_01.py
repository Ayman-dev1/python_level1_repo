# program to read and print the content of a text file
"""
to read a text files
1- open the file
2- read the content
3- close the file
"""

print("----------First way---------")

my_file_refrence = open('D:\\courses to learn\\Python Backend (senior steps)\\my_files\\read_data.txt', 'r')
content = my_file_refrence.read()
print(content)
my_file_refrence.close()

print("---------Second way using clause ignore  close()--------")
with open('D:\\courses to learn\\Python Backend (senior steps)\\my_files\\read_data.txt', 'r') as my_file_refrence:
    content = my_file_refrence.read()
    print(content)






