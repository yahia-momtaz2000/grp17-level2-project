
print('---- sum of all elements in the list -----')
# normal way
def sum_elements(numbers_list):
    sum = 0
    for item in numbers_list:
        sum = sum + item

    return sum
# main program
numbers_list = [3, 5, 4,2 ,1, 7]
result = sum_elements(numbers_list)
print(result)

# Recursion way
def recursive_sum(numbers_list):
    if len(numbers_list) == 0:
        return 0
    else:
        return numbers_list[0] + recursive_sum(numbers_list[1:] )

# main program
numbers_list = [3, 5, 4,2 ,1, 7]
result = recursive_sum(numbers_list)
print(result)


