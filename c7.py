#tut47 join function

list=["sachin","dravid","kohli","yuvraj","bhajji","shewag"]

# for i in list:
#     print(i,"and",end=" ")

a= " , ".join(list)
print(f"{a} and other player")


#tut48 map, filter,reduce

#map  used to convert string to int for type casting

# numbers=["3","44","5"]
# print(map(int,numbers))
# number= list(map(int,numbers))
# number[2]=number[2]+1
# # print(number[2])

# num=[1,2,3,4,5]

# square=list(map(lambda x: x*x,num))
# print(square)

# myList = ['Ram', 'Shyam', 10, 'Bilal', 13.2, 'Feroz'];
# for x in range(len(myList)):
# 	print(myList[x])

#---------------------------------filter
# num_list=[1,2,3,4,5,6,7,8,9]

# def is_greater(num):
#     return num>5

# grTh5=list(filter(is_greater,num_list))
# for i in grTh5:
#     print(grTh5[i])

#---------------------------------reduces

# lst1=[1,2,3,4]
# prod=reduce(lambda x,y:x+y, lst1)
# # num=0
# # for i in lst1:
# #     num = num+i
# print(num)

# dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

# palindromes = list(filter(lambda word: word == word[::-1], dromes))

# print(palindromes)