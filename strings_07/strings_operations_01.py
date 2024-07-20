# show strings functions
print('---- Create and print string ----')
emp_name = 'Ayman Elwan'
print(emp_name)
print(type(emp_name))

print('-------- upper(), lower() functions -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(emp_name)
print(upper_emp_name)
print(lower_emp_name)
print('------ isupper(), islower(), isalpha() functions --- True , False --')
print(upper_emp_name.isupper())
print(lower_emp_name.islower())
print(emp_name.isupper())
print(emp_name.isalpha())
emp_code = '1001'  # string
print(emp_code.isdigit())
emp_code = '1001abc'  # string
print(emp_code.isalnum())  # true letters or digits
emp_sign = '&^%%$'
print(not emp_sign.isalnum())

print('-------------- endsWith() function -----------------')
file_path = 'c:/MyDocuments/egypt.jpg'
file_path = file_path.lower()  # ignore case sensitive
if file_path.endswith('pdf'):
    print("it's a Book")
elif file_path.endswith('jpg'):
    print('It Is An Image')
elif file_path.endswith('mp4'):
    print('It is a video')
else:
    print('Unknown Type')

print('-------------- startswith() function ---------')
emp_mobile = '0124774833'

if emp_mobile.startswith('010'):
    print('it is Vodafone')
elif emp_mobile.startswith('011'):
    print('It is Etisalat')
elif emp_mobile.startswith('012'):
    print('It Is a Orange')

print('------ in membership --------------')
emp_cv = 'I am a programmer, iam interest in c++, java, python'
if 'python' in emp_cv:
    print('This is the wanted employee')
else:
    print('This is not the wanted one ')

print('-------------- count function -----------')
emp_cv = 'iam a python programmer, iam interest in python, java, c++'
print(emp_cv.count('python'))
# loop over string words

print('---------- index(),  replace() functions |  slicing---------------')
emp_email = 'ayman.elwan@gmail.com'
user_name = emp_email[:emp_email.index('@')]  # ayman.elwan
print(user_name)
domain_name = emp_email[emp_email.index('@') + 1:]
print(domain_name)
real_name = user_name.replace('.', ' ')
print(real_name)

print('--------------- Looping :  Loop over letters of string -----------------------')

emp_email = 'ayman.elwan@gmail.com'

print('----- 1. loop using for i loop index -----')
for i in range(len(emp_email)):
    print(emp_email[i])  # slicing

print('----- 2. loop using for each loop index -----')
for letter in emp_email:
    print(letter)

print('------- Split function the String into List of Words -------')
my_courses = 'java python oracle linux php ccna'
courses_list = my_courses.split()  # convert from string to list
print(courses_list)
courses_list.reverse()
courses_list.append('networking')
print(courses_list)

print('------ return the list back to string using join() function --------')
new_courses = '$'.join(courses_list)  # convert list to string
print(new_courses)
print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')
# strip()  ==> removes any spaces at the beginning  and any spaces at the end of string
test = '       Ayman Elwan   '
with_strip = test.strip()
print(with_strip)
print('----------------------------------------')
# title() ==> Make every first letter capital
test_2 = 'maged ahmed'
with_title = test_2.title()
print(with_title)
print('----------------------------------------')
# swapcase() ==> reverse every uppercase to lowercase and vice versa
test_3 = 'MO Salah'
with_swapcase = test_3.swapcase()
print(with_swapcase)
print('----------------------------------------')
# find() ==> It finds the index of the first occurrence of the word you input
test_4 = 'Hi, welcome, welcome'
with_find = test_4.find('welcome')
print(with_find)
print('----------------------------------------')
# rfind() ==> It find the index of the first occurrence of thr word you input
test_5 = 'welcome, Hi, welcome'
with_rfind = test_5.rfind('welcome')
print(with_rfind)
