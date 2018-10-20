'''
Create a Employee Resource Planning Project
Using classes , Exception Handling , Inheritance.
and also create the files in  Presentation Layer(PL) and Business Logic Layer (BLL)


Enmployee A  has ID , Name , Type

Director
share

Manager
area
salary

Teacher
subject
salary

Employee B   has Salary

Manager
Teacher

ID should be SELF GENERTOR.

'''


class EmployeeA:
    def __init__(self, name, id, department):
        self.__name = name
        self.__id = id
        self.__department = department


class EmployeeB:
    def __init__(self,salary):
        self.__salary = salary

class Director(EmployeeA):
    def __init__(self,share):
        self.__share = share

class Manager:
    def __init__(self,area):
        self.__area = area
class Teacher:
    def __init__(self,Subject):
        self.__subject = subject
