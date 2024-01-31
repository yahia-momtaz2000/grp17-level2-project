print('--- program to use factorial ----')
# The factorial of 6 is denoted as 6! = 1*2*3*4*5*6 = 720.
number = 6
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i

print(factorial)

print('----- using Recursion ----------------')
def recursion_factorial(number):
    if number == 1:
        return number
    else:
        return number * recursion_factorial(number - 1)

# main program
number = 6
result = recursion_factorial(number)
print(result)