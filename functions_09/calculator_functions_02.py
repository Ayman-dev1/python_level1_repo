# create 4 functions
"""
1. add_numbers : which add 2 parameters and return result
2. multiply_numbers : which multiply 3 parameters and return result
3. divide_numbers : which divide 2 parameters and return result and check not to divide by Zero
4. abs_numbers : which take 1 parameter : if it is negative just return +ive of this number
"""


def add_numbers(first_num, second_num):
    return first_num + second_num


def multiply_numbers(first_num, second_num, third_num):
    return first_num * second_num * third_num


def divide_numbers(first_num, second_num):
    if second_num == 0:
        return 'Error - Cannot divide by zero'
    else:
        return first_num / second_num


def abs_number(value):
    if value < 0:
        return value * (-1)
    else:
        return value


# main program
#calling functions
add_result = add_numbers(7, 8)
multiply_result = multiply_numbers(9, 6, 3)
divide_result = divide_numbers(8, 2)
abs_result = abs_number(-3)
print(add_result, multiply_result, divide_result, abs_result)
