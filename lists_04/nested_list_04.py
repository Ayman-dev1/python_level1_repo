# program to show nested list operations
nested_list = [
                [101, 'Ayman', 'Cairo'],
                [202, 'Maged', 'Giza'],
                [303, 'Loay', ['cairo', 'Nasr City', 'Abbas El Akkad']]
              ]

print(nested_list)
# print the first element [101, 'Ayman', 'Cairo']
print(nested_list[0])

# print alex
print(nested_list[1][2])

# print nasr city
print(nested_list[2][2][1])

# add this list to Nested_list
new_person = [104, 'Amir', 'Gharbeya']

nested_list.append(new_person)
print(nested_list)
