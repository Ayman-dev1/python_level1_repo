import csv


def password_validation(pass_value):
    count_upper, count_lower, count_digits, count_signs = 0, 0, 0, 0

    if len(pass_value) > 8:
        for letter in pass_value:
            if letter.isupper():
                count_upper = count_upper + 1
            elif letter.islower():
                count_lower = count_lower + 1
            elif letter.isdigit():
                count_digits = count_digits + 1
            elif not letter.isalnum():
                count_signs = count_signs + 1
        if count_lower >= 1 and count_upper >= 1 and count_signs >= 1 and count_digits >= 1:
            return True


with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\passwords.csv", 'r') as my_file1:
    reader_pen = csv.reader(my_file1)
    passwords = [row[0] for row in reader_pen]

with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\valid_passwords.csv", 'w') as my_file2:
    writer_pen = csv.writer(my_file2)
    for item in passwords:
        if password_validation(item):
            writer_pen.writerow(item)


