#tut8

mystr = "Harry is a good boy"
print(len(mystr))
print(mystr[::])

print(mystr[0::2])
print(mystr[3:9])
print(mystr[::-1])

print(type(mystr))
#alpha numeric check
print(mystr.isalnum())

#alpha  check
print(mystr.isalpha())

#end with  check
print(mystr.endswith("boy"))
print(mystr.endswith("boyss"))

#count
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))

#tut9
print("-----------------list-------------")
grocery=["Harpic","vim bar","deodrant","bhindi",111]
print(grocery)
print(grocery[0])
print(grocery[4])

number=[2,4,6,8,10]
print(number[2])
print(number.reverse())
print(number)
print(number.sort())
print(number)
print(number[:3])
print(number[1:])
print(number[1:4])
print(number[::2])
print(number[::-2])

#append
number.append(7)
print(number)

number.insert(2,33)
print(number)

number.remove(6)
print(number)
number.pop()
print(number)

number[1]=99
print(number)

#mutable  -can be change  (list)
#immutable  - cant be change (tupple)
tp=(1,2,3,4)
print(tp)

#error get 
#tp[1]=5

#change
a=5
b=10
print(a,b)
tmp=a
a=b
b=tmp
print(a,b)

a ,b =b,a

print(a,b)


print("______________tut10___________________")

d1={}
print(type(d1))

d2={"monday":"AI","Tuesday":"ML","Wendsday":"CP","Thursday":{"SIP":"VIVA","MINIPROJECT":"REPORt"}}
print(d2)
print(d2["Tuesday"])
print(d2["Thursday"])
print(d2["Thursday"]["SIP"])
print(d2.keys())
print(d2.items())


print("____________tuto12____________")
s=set()
print(type(s))
s.add(11)
print(s)
s.add(2)
print(s)
s1=s.union({12})
print(s1)
s1=s.intersection({121,2,3,4,5,6})
print(s1)
print(max(s1))
print(min(s1))

print("________tuto13______________")

v1=3
v2=5
if v1>v2:
    print("v1 greater")
else:
    print("v2 greater")


print("______tut16____")
list1 =[ ["harry",1], ["Larry",2], ["Carry",3]]

for item, lol in list1:
    print(item,"and lolly is ", lol)

items = [1,22,33,4,5,66,8]
for item in  items:
    if str(item).isnumeric() and item>6:
        print(item)

print("______tut17_____")

i=0
while(i<5):
    print(i)
    i+=1

i=0
while(True):
    if i+1<3:
        i=i+1
        continue
    print(i, end=" ")
    if i==5:
        break #stop the loop
    i+=1

while(True):
    no = int(input("Enter Number:"))

    if no > 100:
        print("Congrates you have enter no > 100")
        break
    else:
        print("Try again")
        continue