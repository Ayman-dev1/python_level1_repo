# program to write list content to a csv file
import csv

people_list = [
    ['Name', 'Age', 'City'],
    ['Adham', 25, 'Assuit'],
    ['Esam', 30, 'Cairo'],
    ['Shady', 30, 'Mansoura'],
    ['Ayman', 20, 'Cairo']
]

with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\people.csv", 'w',
          newline='') as my_file_reference:
    write_pen = csv.writer(my_file_reference)
    for item in people_list:
        write_pen.writerow(item)
