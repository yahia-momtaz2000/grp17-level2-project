
from employee import Employee

# main program
print('-==== Create new object ======')
emp_ahmed = Employee(101, 'Ahmed Esam', 7000, 'Dev', 10, 20.0)
print(f'Ahmed Monthly net salary = {emp_ahmed.calc_monthly_net_salary()}')
print(f'Ahmed Annual net salary = {emp_ahmed.calc_annual_net_salary()}')


print('=================== Method Overriding ==========================')
emp_ahmed.print_person_details()
