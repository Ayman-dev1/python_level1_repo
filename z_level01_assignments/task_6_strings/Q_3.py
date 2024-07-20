# program to make half of string upper case

str1 = 'ArabRepublicOfEgypt'
print('The Original String: ', str1)


half = len(str1) / 2
half = int(half)
statment = str1[:half].lower() + str1[half:].upper()


print('The Resultant string: ',statment)
