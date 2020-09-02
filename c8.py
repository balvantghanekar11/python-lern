dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

#exe1 map

numbers=["3","44","5"]
print(map(int,numbers))
number= list(map(int,numbers))
number[2]=number[2]+1
print(number[2])


#exe2 map

num=[1,2,3,4,5]

square=list(map(lambda x: x*x,num))
print(square)

#-------- filter

num_list=[1,2,3,4,5,6,7,8,9]

def is_greater(num):
    return num>5

grTh5=list(filter(is_greater,num_list))
print(grTh5)


#--------------------------reduce

from functools import reduce

lst1=[1,2,3,4]
num=reduce(lambda x,y:x+y, lst1)
# num=0
# for i in lst1:
#     num = num+i
print(num)