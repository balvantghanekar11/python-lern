#___tut30  seek tell fun file


f= open("myfile.txt")
print(f.tell()) # where is file pointer 

print(f.readline())
print(f.tell())
f.seek(10)  # move file pointer to 10th position
print(f.readline())
print(f.tell())


#____with block
print("With block\n\n")
with open("myfile.txt") as f:
    a=f.read(4)
    print(a)
    # print(f.readlines())
#     print(f.readline())

# f.close()


#Global keyword and global variable

print("global__\n")
l=10    #global variable
def fun1(n):
    # l=5
    m=8   #local
    global l    #global keyword
    l=l+33  
    print(l,m)
    print(n,"I have printed")

fun1("This is me")


def harry():
    x=30
    def jak():
        global x
        x=44
    print("before calling jak",x)   
    jak()
    print("after calling jak",x)

harry()



# pattern

num=int(input("Enter num of rows"))
bol=input("enter 1 or 0")
if bol=="1":
    for i in range(0,num+1):
        print("*"*i)
    
if bol=="0":
    for i in range(num,0,-1):
        print("*"*i)