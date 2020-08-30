print("______tut21_____")


#operators

#Arithmatic

print("5+6:",5+6)
print("5-6:",5-6)
print("5/6:",5/6)
print("5*6:",5*6)
print("5%5:",5%5)
print("5//6:",5//6)  #floor division int return
print("5**6:",5**6)
#Assignment
print("Assignment operator")
x=5
print(x)
x+=7
print(x)

#comparision
print("comparision operator")
i=5
print(i>5)
print(i<5)
print(i==5)

#logical
a=True
b=False

print(a is not b)

#membership
list=[1,2,3,4,5,6,7,8]
print(4 not in list)

#bitwise
#& | 

print("______________Function")

a=4
b=6

c=sum((a,b))  #built in fun
print(c)

def fun():
    print("Fun print")

fun()           #fun valu print
print(fun())    #return value print

def average(a,b):
    """This is a function which will calculate average of two number Doc value"""
    avg=(a+b)/2
    print("fun value avg :",avg)
    return avg

ans=average(3,4)
print("Fun return value print:",ans)
print(average.__doc__)    #doc valu print of function
