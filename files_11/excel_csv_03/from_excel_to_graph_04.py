# program to read Excel file csv and plot chart
import csv

import matplotlib.pyplot as plt

with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\people.csv", 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)
    reader_pen.__next__() # skip the first row  [header]
    x_axis = []
    y_axis = []
    for row in reader_pen:
        x_axis.append(row[0]) # names
        y_axis.append(float(row[1]))


    plt.bar(x_axis, y_axis)
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.title('Bar Chart from csv Data')
    plt.xticks(rotation=45)
    plt.show()
