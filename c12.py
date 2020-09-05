#tut61 multiple inheritance

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

class Player():

    def __init__(self,aname,game):
        self.name=aname
        self.game=game

    def disp(self):
        return f" Programmers Name : {self.name} your game is {self.game}"

class CoolProgrammer(Employee,Player):
    pass

harry = Employee("Harry",344,"HR")
harry1=Player("harray1",["Cricket", "Pubg"])
karan=CoolProgrammer("karan",444,"HR")
print(harry.display())
print(harry1.disp())
print(karan.display())