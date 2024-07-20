str1 = input('Enter String: ').lower()  # Hello world world Python is great great python
after_op = []
string_list = str1.split()
for item in string_list:
    if item not in after_op:
        after_op.append(item)
a = ' '.join(after_op)
print(a)
