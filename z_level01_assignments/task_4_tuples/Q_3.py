company_employees = [
    (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
    (103, 'Adham Aly', 5000.0, 'Engineer', 'M'),
    (104, 'Islam Hassan', 7000.0, 'Sales', 'M'),
    (105, 'Marwa Esam', 7000.0, 'Marketer', 'F'),
    (106, 'Ola Hassan', 7000.0, 'Engineer', 'F')
]

male_count, female_count = 0, 0

for gender in company_employees:
    if gender[4] == 'M':
        male_count += 1
    elif gender[4] == 'F':
        female_count += 1

print("Number of Males:", male_count)
print("Number of Females:", female_count)
