#tut51 decorators

def myfun():
    print("Subscribe now")

func2=myfun
func2()

def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
    
a=funcret(0)
print(a)
print("\n\n Decoraotrs \n")
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Exexuted")
    return nowexec
@dec1
def who():
    print("Harry is a good boy")
#who=dec1(who)
who()



###2

def fun1(fun3):
    print("hello")
    fun3(*args,*kwargs)
    print("how r u")
    return fun1

@fun1
def fun2(name):
    print(f"{name}")

fun2("blu")