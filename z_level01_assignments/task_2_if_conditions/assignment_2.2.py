operator = int(input("Enter operator (1,2,3,4 = +, -, *, /): "))
first_num = int(input("Enter First num: "))
sec_num = int(input("Enter Sec Number: "))

if operator == 1:
    result = first_num + sec_num
    print(first_num, '+', sec_num, ' = ', result)
elif operator == 2:
    result = first_num - sec_num
    print(first_num, '-', sec_num, ' = ', result)
elif operator == 3:
    result = first_num * sec_num
    print(first_num, '*', sec_num, ' = ', result)
elif operator == 4:
    result = first_num / sec_num
    print(first_num, '/', sec_num, ' = ', result)
else:
    print("Error")

print("The result is:", result)
