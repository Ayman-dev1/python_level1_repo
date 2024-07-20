# program to read from Excel file into a List
import csv

new_people_list = []
with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\people.csv", 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)

    for row in reader_pen:
        new_people_list.append(row)

print(new_people_list)
