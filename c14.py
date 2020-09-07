#t66 dimond problem multiple inheritance

class A:
    
    def disp(self):
        print("Class A method")

class B(A):
    def disp(self):
        print("Class B method")

class C(A):
    def disp(self):
        print("Class C method")

class D(B,C):
    def disp(self):
        print("Class D method")

a=A()
b=B()
c=C()
d=D()

d.disp()


# tut 62

class dad:
    basket=1

class son(dad):
    dance=1

    def isdance(self):
        return f"Yes i dance {self.dance}"

class Grandson(son):
    dance=6

    def isdance(self):
        return f"Jackson Yes i dance {self.dance}"


c1=dad()

