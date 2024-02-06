import sys


class Emp:
    # __init__  : class constructor : initialize object data with values
    # instance attributes : emp_id, emp_name, emp_gross_salary, emp_job
    def __init__(self, emp_id, emp_name, emp_gross_salary, emp_job):
        self.__emp_id = emp_id
        self.__emp_name = emp_name
        if emp_gross_salary > 0:
            self.__emp_gross_salary = emp_gross_salary
        else:
            print('Salary cannot be -ve _ invalid value')
            sys.exit()
        self.__emp_job = emp_job

    # Accessors [ Getters and Setters ]
    def get_emp_name(self):
        return self.__emp_name

    def set_emp_name(self, new_emp_name):
        self.__emp_name = new_emp_name

    def get_emp_gross_salary(self):
        return self.__emp_gross_salary

    def set_emp_gross_salary(self, new_emp_gross_salary):
        if new_emp_gross_salary > 0:
            self.__emp_gross_salary = new_emp_gross_salary
        else:
            print('Salary cannot be -ve _ invalid value')
            sys.exit()



    # instance methods [ functions ]

    def calc_monthly_net_salary(self):
        tax = 10    # assume
        return self.__emp_gross_salary - self.__emp_gross_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12

