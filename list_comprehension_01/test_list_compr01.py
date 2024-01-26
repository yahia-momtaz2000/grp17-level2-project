my_list = [4, 6, 5, 7, 3, 2, 16, 20]
print('--- assign a list to new list using normal way ----')
new_list = []
for item in my_list:
    new_list.append(item)
print(new_list)

print('--- assign a list to new list using List comprehension way ----')
new_list = [item for item in my_list]
print(new_list)

print('--- Create new list with numbers from 1 to 10 Using List Comprehension ---- ')
numbers_list = [i for i in range(1, 11)]
print(numbers_list)

print('---- Double items * 2 to new list Using List Comprehension -----')
double_list = [item * 2 for item in my_list]
"""
double_list = []
for item in my_list:
    double_list.append(item * 2)
"""

print('--- create new list of letters from a string Using List Comprehension ----')
my_password = 'yahia2030'
letters_list = [letter for letter in my_password]
print(letters_list)

print('------  create new list add only even numbers Using List Comprehension  -----')
even_list = []
for item in my_list:
    if item % 2 == 0:
        even_list.append(item)
print(even_list)

even_list = [item for item in my_list if item % 2 == 0]
print(even_list)

print('----- create new list return price or invalid price if -ve Using List Comprehension-----')
prices_list = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices_list = [item if item > 0 else 'Invalid' for item in prices_list]
print(new_prices_list)

print('----- Recreate the last example using def function ------') # use def is required in case we need if elif else or any complex process
def validate_price(price):
    return price if price > 0 else 'Invalid'   # conditional expression : ternary operator ( only found with ( if only ) or ( if else )

prices_list = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices_list = [validate_price(item) for item in prices_list]
print(new_prices_list)