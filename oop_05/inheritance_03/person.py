
class Person:
    def __init__(self, person_id, person_name, person_gross_salary, person_job):
        self.__person_id = person_id
        self.__person_name = person_name
        self.__person_gross_salary = person_gross_salary
        self.__person_job = person_job

    # Extra Methods
    def print_person_details(self):
        print(f'Person id = {self.__person_id}')
        print(f'Person name = {self.__person_name}')

    # Accessors : Getters & Setters
    def get_person_gross_salary(self):
        return self.__person_gross_salary

    def set_person_gross_salary(self, person_gross_salary):
        self.__person_gross_salary = person_gross_salary

