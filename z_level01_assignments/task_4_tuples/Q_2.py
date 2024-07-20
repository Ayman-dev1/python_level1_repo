company_employees = [
    (101, 'Ahmed Esam', 10000.0, 'Cairo'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Cairo'),
    (103, 'Adham Aly', 5000.0, 'Cairo'),
    (104, 'Islam Hassan', 7000.0, 'Cairo')
]

sum_salary = 0
for salary in company_employees:
    sum_salary = sum_salary + salary[2]


print('sum:', sum_salary)
