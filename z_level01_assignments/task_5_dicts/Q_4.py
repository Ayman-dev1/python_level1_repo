shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}

for key in shopping_cart_dict:
    shopping_cart_dict[key] = shopping_cart_dict[key] + 0.1 * shopping_cart_dict[key]
print('After 10% raise = ', shopping_cart_dict)

total = sum(shopping_cart_dict.values())
print('Total = ', total)
total_net = total + 0.14 * total
print('Total net = ', total_net)
