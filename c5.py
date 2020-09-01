#____tut36 lambda anonymous function

def add(a,b):
    return a+b

minus= lambda x,y:x-y
print(minus(5,4))

def a_first(a):
    return a
list=[[1,2],[4,5],[8,7]]
list.sort(key=a_first)
print(a_first)


#tuto38

import random

random_number=random.randint(0,5)
rand=random.random()
print(random_number)
print(rand)

lst=["aa","bb","cc","dd","ee","ff","gg","hh","ii"]
choice=random.choice(lst)
print(choice)

# tut39fstring
import math
me="Harry"
al=3
a="this is %s %s"%(me,al)
a="this is {1} {0}"
b=a.format(me,al)
print(b)

a=f"this is {me} {al} {4*55} {math.cos(65)}"
print(a)


# tut41 args kwargs
# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)

def funargs(normal,*args,**kwarga):
    print(normal)
    for i in args:
        print(i)
    print("Now i would like to intro heros")
    for key,value in kwarga.items():
        print(f"{key} is {value}")

# function_name_print("Harry","Rohan","Skillf","Hammad","Shivam")

har=["Harry","Rohan","c","d","e"]
normal="Normal argument"
kw={"aa":"zz","bb":"yy","cc":"xx"}
funargs(normal,*har,**kw)


#tut42time

import time

initial =time.time()
print(initial)
k=0
while k<5:
    print("this is blu")
    time.sleep(2)
    k+=1
print("while loop ran in",time.time()-initial,"Seconds")

initial2=time.time()
for i in range(45):
    print("Blu")
print("For loop ran in",time.time()-initial2,"Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

