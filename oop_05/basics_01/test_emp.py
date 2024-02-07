from emp import Emp     # from emp module import Emp class

# main program
print('---- Take object emp_ahmed from class Emp in module emp ----')
# create new object[new instance ] from the class and initializa the instance by the initial values
# through the constructor
emp_ahmed = Emp(101, 'Ahmed Esam', 7000, 'Programmer')
# emp_ahmed.emp_gross_salary = -8000  # Direct access to attributes   ->>  To Solve this ;; attributes should be private [ no direct access ]
emp_ahmed.set_emp_gross_salary(8000)

# print(f'emp ahmed name = {emp_ahmed.emp_name}')
print(f'emp ahmed name = {emp_ahmed.get_emp_name()}')


# print(f'emp ahmed gross salary = {emp_ahmed.emp_gross_salary}')
print(f'emp ahmed gross salary = {emp_ahmed.get_emp_gross_salary()}')

print(f'emp ahmed monthly net salary {emp_ahmed.calc_monthly_net_salary()}')
print(f'emp ahmed annual net salary {emp_ahmed.calc_annual_net_salary()}')

print('----- object emp_marwa from Emp class ------------')
emp_marwa = Emp(102, 'Marwa Hassan', 9000, 'Python developer')
emp_marwa.set_emp_gross_salary(12000)      # change [ set ] value
print(f'emp marwa monthly net salary {emp_marwa.calc_monthly_net_salary()}')
print(f'emp marwa annual net salary {emp_marwa.calc_annual_net_salary()}')

print('----- object emp_hesham from Emp class ------------')
emp_hesham = Emp(103, 'Hesham Awad', 6000, 'Java developer')

print('================== Put objects in List of Employees ==========================')
emps_list = [emp_ahmed, emp_marwa, emp_hesham]
emps_list.append(   Emp(104, 'Farouk Aly', 14000, 'Project Manager')  )

sum = 0
for employee in emps_list:
    print(f'Emp name = {employee.get_emp_name()}, emp net salary = {employee.calc_monthly_net_salary()}')
    sum = sum + employee.calc_monthly_net_salary()
print(f'Sum of net salary = {sum}')




