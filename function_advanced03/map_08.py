import math

print('--- : Loop over the list and cube each element -----')
numbers_elements = [4, 5, 2, 10, 3]

# normal way
cubic_list = []
for item in numbers_elements:
    cubic_list.append(item ** 3)
print(cubic_list)

# using map function
def get_cubic(number):
    return number ** 3

cubic_list = list( map(  get_cubic, numbers_elements )  )
print(cubic_list)

# using Lambda with map
cubic_list = list( map( lambda number : number ** 3, numbers_elements )  )
print(cubic_list)


