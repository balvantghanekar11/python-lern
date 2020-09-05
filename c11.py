#tut59-60 abstraction encapsulation


class Employee:

    no_of_leaves=9

    def __init__(self,name,salary,role):
        self.name= name
        self.salary=salary
        self.role=role

    def display(self):
        return f"Name : {self.name} your salary is {self.salary} and Your role is {self.role} ."

    @classmethod
    def changeNoOfLeaves(cls,newLeaves):
        cls.no_of_leaves=newLeaves

    @staticmethod
    def printgood(string):
        print("This is good" + string)

class Programmer(Employee):

    def __init__(self,aname,asalary,arole,languages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=languages

    def disp(self):
        return f" Programmers Name : {self.name} your salary is {self.salary} and Your role is {self.role} languages are : {self.languages}"

harry = Employee("Harry",344,"HR")
harry1=Programmer("harray1",122,"Self",["Python","cpp"])
print(harry.display())
print(harry1.disp())