# program to show list of dictionaries operations
persons_list = [{101: 'Omar', 102: 'Esraa', 103: 'Ibrahim'}]
print(len(persons_list))

# print {101: 'Omar', 102: 'Esraa', 103: 'Ibrahim'}
print(persons_list[0])

# print Esraa
print(persons_list[0][102])

print('----loop over dict keys : values---')
for key, value in persons_list[0].items():
    print(key, value)

print('-----Add new dict to the list------')
students_dict = {104: 'Ayman', 105: 'Ramy'}
persons_list.append(students_dict)
print(persons_list)

# print Ayman
print(persons_list[1][104])

