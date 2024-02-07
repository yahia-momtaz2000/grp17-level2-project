from employee import Employee

# main program

print(f'No of Employees objects = {Employee.no_of_employees}')
emp_hossam = Employee(101, 'Hossam Hassan', 7000, 'dev', 3000)
emp_heba = Employee(102, 'Heba Mostafa', 5000, 'doctor', 1500)
print(f'No of Employees objects = {Employee.no_of_employees}')

print(f'Hossam wallet = {emp_hossam.get_emp_wallet()}') # 3000
print(f'Heba wallet = {emp_heba.get_emp_wallet()}')  # 1500
print(f'total bonus = {Employee.total_bonus}')       # 20000

emp_hossam.receive_bonus(2500)
emp_heba.receive_bonus(1200)
emp_heba.receive_bonus(1500)
print('----------------')
print(f'Hossam wallet = {emp_hossam.get_emp_wallet()}') # 5500
print(f'Heba wallet = {emp_heba.get_emp_wallet()}')  # 4200
print(f'total bonus = {Employee.total_bonus}')       # 14800
