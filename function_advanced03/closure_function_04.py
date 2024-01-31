
print('--- Create inner function used to change '
      'variable from outer function and the change is '
      'still referenced from the namespace ----')

def outer_function(name, salary):
    def inner_function(address):
        nonlocal salary
        salary = salary + 5000
        print(name, salary, address)
    return inner_function

# main program
function_reference = outer_function('Yahia', 6000)
function_reference('Cairo')     # calling inner function



print('----- # Free variables references from namespace and still change them ---- ')
def outer_function(name, salary):
    def inner_function(bonus):
        nonlocal salary
        salary = salary + bonus
        print(name, salary)
    return inner_function

# main program
function_reference = outer_function('Ehab', 6000)
function_reference(2000)    # 8000
function_reference(3000)    # 11000
function_reference(3000)    # 14000

