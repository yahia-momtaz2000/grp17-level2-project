import math

print('--- # Make a number power to a value using lambda  -----')
# normal function
def power_function(num, pow):
    return math.pow(num, pow)

# main program
result = power_function(2, 4)
print(result)

# Convert to lambda function [ anonoymous function ]
function_reference = lambda num, pow : math.pow(num, pow)
result = function_reference(4, 3)
print(result)



