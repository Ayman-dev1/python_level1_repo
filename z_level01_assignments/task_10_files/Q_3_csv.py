
import csv

with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\people.csv", 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)
    reader_pen.__next__()
    total = 0
    avg = 0
    count = 0
    for row in reader_pen:
        total = total + int(row[1])
        count += 1
        avg = total / count

print('Average from column 1 : ', avg)

