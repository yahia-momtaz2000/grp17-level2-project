print('Set creation and printing')
my_set = {15, 20, 4, 3, 15, 20, 17, 4}
print(type(my_set))
print(my_set)


print('---- add new elements : no index  ---')
my_set.add(33)
print(my_set)


print('----- Find elements hint : no index ------')
is_found = 34 in my_set
print(is_found)


print('------- Change element : no index  55 instead of 15 ------')
my_set.remove(15)
my_set.add(55)
print(my_set)


print('---- Count element -------')
print(len(my_set))


print('------ Loop over elements using foreach loop ---------')
for item in my_set:
    print(item)


print('------ Remove Element --- discard() remove() pop() --------')
my_set.remove(33)
my_set.discard(20)
my_set.pop() # XXX
print(my_set)


print('-------- Sort set ----------')
my_set = sorted(my_set)
print(my_set)


print('---------- Convert from List to set and vice versa ------- ')
my_list = [15, 6, 22, 30, 15, 10, 22, 6]
new_set = set(my_list)
print(new_set)
my_list = list(new_set)
print(my_list)