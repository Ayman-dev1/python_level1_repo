book_dict = {'Pages': 277, 'name': 'Gone girl', 'year': 2007}

print('----- Adding new element ( author ) To a Dictionary -----')
book_dict['author'] = 'Ayman Elwan'
print(book_dict)

print('------ Accessing Elements ( name ) inside a Dictionary -------')
print(book_dict['name'])

print('---- Changing Elements inside a Dictionary year to 2010 -----')
book_dict['year'] = 2010
print(book_dict)

print('----- Use Loop to print keys and values -----')
for key, value in book_dict.items():
    print(key, value)

print('----- Removing Item ( name ) from a Dictionary ------')
book_dict.pop('name')
print(book_dict)

