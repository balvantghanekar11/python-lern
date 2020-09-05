#tut65 super() and overriding

class A:
    var1= "I am variable of class A"
    def __init__(self):
        self.v1="I am inside class A's constructor"
        self.var1="new instance classA"
        self.special="Special "
    
class B(A):
    var1="I am in class B"
    def __init__(self):
        super().__init__()
        self.v1="I am class b constructor"
        self.var1="Instance var in class B"

a=A()
b=B()

print(b.special, b.var1,b.v1)