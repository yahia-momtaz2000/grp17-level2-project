# packing elements
def sum_unknown_numbers(*my_numbers):   # tuple
    print(type(my_numbers)) # tuple
    return sum(my_numbers)


# main program
sum_result = sum_unknown_numbers(6, 22, 10, 20)
print(sum_result)