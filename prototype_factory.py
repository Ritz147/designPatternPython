import copy
class Address:
    def __init__(self , street_address , suite , city):
        self.suite=suite
        self.city=city
        self.street_address=street_address

    def __str__(self):
        return f'{self.street_address},Suite #{self.suite} , {self.city}'
class Employee:
    def __init__(self,name,address):
        self.address=address
        self.name=name
    def __str__(self):
        return f'{self.name} works at {self.address}'
class EmployeeFactory:
    main_office_employee=Employee('',Address('123 East Drive',0,'London'))
    auxillary_office_employee=Employee('',Address('123B East Drive',0,'London'))
    @staticmethod
    def __new_employee(proto,name,suite):
        result=copy.deepcopy(proto)
        result.name=name
        result.address.suite=suite
        return result
    @staticmethod
    def new_main_office_employee(name,suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)
    @staticmethod
    def new_auxillary_office_employee(name,suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.auxillary_office_employee, name, suite)
john=EmployeeFactory.new_main_office_employee('John',101)
jane=EmployeeFactory.new_auxillary_office_employee('Jane',102)
print(john)
print(jane)

