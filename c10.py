#tut53 oop class object

class student:
    pass

blu1=student()
blu2=student()

blu1.name="raju"
blu1.std=12
blu1.sec="MCA"
blu2.std=11
print(blu1.sec,blu2.std)

print(blu1,blu2)


#tut54  '
class Employee:
    no_of_leaves=0
    pass

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=111
harry.role="Instructor"
harry.no_of_leaves=8

rohan.name="Rohan"
rohan.salary=333
rohan.role="stud"
print(harry.salary)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.__dict__)

#tut55  self & __init()__

class Employee2:
    no_of_leaves=8
    pass

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role


    def det(self):
        return f"Name is {self.name} Salary is {self.salary} and role is {self.role}"
        
    #class method
    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leaves=newLeaves

    @classmethod
    def from_str(cls,string):
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

harry1=Employee2("blu",4444,"HR")
# rohan1=Employee2()

# harry1.name="Harry"
# harry1.salary=11111
# harry1.role="HR"

# rohan1.name="rohan"
# rohan1.salary=3333
# rohan1.role="Stud"

# print(rohan1.det())
print(harry1.salary)

# tut56 class method
raju = Employee2("raju",5555,"stud")
raju.change_leaves(33)
karan= Employee2.from_str("karan-2222-HR")
print(Employee2.no_of_leaves)
print(raju.no_of_leaves)

print(karan.name)


#tut58 static

class stud:
    
    @staticmethod
    def printgood(string):
        print("This is good "+string)


karan = stud()
karan.printgood("blu")


