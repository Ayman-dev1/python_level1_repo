# program to show dictionary operations
print('---- create and print dictionary -----')
shopping_cart_dict = {'milk': 40.0,'eggs': 160.0, 'Bread': 30.0}
print(shopping_cart_dict)
print(type(shopping_cart_dict))
print(len(shopping_cart_dict))

print('------ Adding new Key : value, change value of a key to the dictionary -------')
shopping_cart_dict['nescafe'] = 60.0   #Adding New Key : Value
shopping_cart_dict['milk'] = 45.0      # Change = edit = Update the value
print(shopping_cart_dict)

print('------ access element -----')
print('price of eggs = ', shopping_cart_dict['eggs'])
# add 25% to the price of eggs
shopping_cart_dict['eggs'] = shopping_cart_dict['eggs'] + 25/100 * shopping_cart_dict['eggs']
print(shopping_cart_dict)

print('---- delete element pair from dict using pop ------')
shopping_cart_dict.pop('Bread')
print(shopping_cart_dict)

print('------ Concat Multi dictionaries using update function ------')
home_cart_dict = {'Meat': 400.0, 'chicken': 125.0}
shopping_cart_dict.update(home_cart_dict)
print(shopping_cart_dict)
