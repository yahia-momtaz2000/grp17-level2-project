from functools import reduce

print('Calculate the product of all elements in a list using the reduce function')

numbers_list = [2, 3, 4, 5]

# normal way:
multiply_product = 1
for item in numbers_list:
    multiply_product = multiply_product * item

print(multiply_product)

# using reduce function
def multiply_values(val1, val2):
    return val1 * val2

multiply_result = reduce(multiply_values, numbers_list   )
print(multiply_result)

# using lambda
multiply_result = reduce( lambda val1, val2 : val1 * val2, numbers_list   )
print(multiply_result)

