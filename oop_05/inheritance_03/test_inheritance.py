
from employee import Employee
from oop_05.inheritance_03.manager import Manager

# main program
print('-==== Create new object from Employee ======')
emp_ahmed = Employee(101, 'Ahmed Esam', 7000, 'Dev', 10, 20.0)
print(f'Ahmed Monthly net salary = {emp_ahmed.calc_monthly_net_salary()}')
print(f'Ahmed Annual net salary = {emp_ahmed.calc_annual_net_salary()}')

print('-==== Create new object from Manager ======')
mgr_khaled = Manager(401, 'Khaled Rafaat', 15000, 'P.M', 10)
print(f'Khalid Monthly net salary = {mgr_khaled.calc_monthly_net_salary()}')
# print(f'Khalid Annual net salary = {mgr_khaled.calc_annual_net_salary()}')
company_profit = 1_000_000
# print(f'Khalid annual net salary + profit = {mgr_khaled.calc_annual_net_salary_profit(company_profit)}')


print('=================== Method Overriding ==========================')
emp_ahmed.print_person_details()


print('================= OOP Polymorphism ========================')
def print_data_for_all(person):
    if isinstance(person, Employee):                # java :    instanceof
        print('This is an Employee object')
        print(f'id = {person.get_person_name()}')           # from parent class [ Person ]
        print(f'Monthly net salary = {person.calc_monthly_net_salary()}')     # from the child class [ Employee ]
    elif isinstance(person, Manager):
        print('This is a Manager')
        print(f'id = {person.get_person_name()}')  # from parent class [ Person ]
        print(f'Monthly net salary = {person.calc_monthly_net_salary()}')  # from the child class [ Manager ]
    else:
        print('This is unknown object')


# test poly
print_data_for_all(emp_ahmed)
print('----')
print_data_for_all(mgr_khaled)

print('================= OOP Abstraction ========================')
# create new object ??          child or from parent ???           >>>>>  we always take object from [[ child class ]]
# abstract class    =   it is the class that is not instantiated [ class cannot have objects ]
#                       it also can contains abstract methods
# abstract method   = it is a method without body created in abstract class
#                       all children MUST override it