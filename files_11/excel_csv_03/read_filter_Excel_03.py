# program to read a csv file, Filter data by city = Cairo
import csv

with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\people.csv", 'r') as my_file_reference1, \
    open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\people_cairo.csv", 'w', newline='') as my_file_reference2:
    reader_pen = csv.reader(my_file_reference1)
    writer_pen = csv.writer(my_file_reference2)
    writer_pen.writerow(['Name', 'Age', 'City'])
    for row in reader_pen:
        if row[2].lower() == 'Cairo'.lower():
            writer_pen.writerow(row)

