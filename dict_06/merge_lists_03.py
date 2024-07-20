# program to merge 2 lists into a dictionary
emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']

# create empty dict
persons_dict = {}

for i in range(len(emp_ids_list)):
    # print(i, emp_ids_list[i], emp_names_list[i]) # to understand this section
    persons_dict[emp_ids_list[i]] = emp_names_list[i]  # fill the dict

print(persons_dict)
