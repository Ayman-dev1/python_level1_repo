# program to validate complex password
password = 'Egypt_2024' # valid
count_upper, count_lower, count_digits, count_signs = 0, 0, 0, 0

if len(password) > 8 :
    for letter in password:
        if letter.isupper():
            count_upper = count_upper + 1
        elif letter.islower():
            count_lower = count_lower + 1
        elif letter.isdigit():
            count_digits = count_digits + 1
        elif not letter.isalnum():  # signs
            count_signs = count_signs + 1

    if count_upper >= 1 and count_lower >= 1 and count_digits >= 1 and count_signs >= 1:
        print('Valid Password')
    else:
        print('Invalid Password')
else:
    print('Invalid password, should be > 8 letters')