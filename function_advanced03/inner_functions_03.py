
print('-- 1 - Create inner function used to print variable from outer function---')
def outer_function(name):
    def inner_function():
        print(f'Hello {name}')
    print(f'Hi {name}')
    inner_function()

# main program - Call outer function
outer_function('Yahia Momtaz')


print('-- 2 -- Create inner function used to change variable from outer function ----')
def outer_function(name, salary):
    def inner_function():
        # nonlocal salary
        salary = 5000
        print('inner print : ', name, salary)  # 5000
    inner_function()
    print('outer print : ',name, salary)   # 6000

# main program - call outer function
outer_function('Yahia', 6000)






print('-- 3 -- # Create inner function used to change variable '
      ' from outer function and the change is still referenced from'
      ' the outer function ----')
def outer_function(name, salary):
    def inner_function():
        nonlocal salary
        salary = salary + 5000
        print('inner print : ', name, salary)  # 11000
    inner_function()
    print('outer print : ',name, salary)   # 11000

# main program - call outer function
outer_function('Yahia', 6000)

