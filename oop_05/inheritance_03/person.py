from abc import ABC, abstractmethod


class Person(ABC):
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

    def get_person_id(self):
        return self.__person_id

    def get_person_name(self):
        return self.__person_name
        # return self.get_person_name()       # recursion

    @abstractmethod     # [ all children must override this method ]
    def calc_annual_net_salary(self):
        pass
