#tut37
def getdate():
    import datetime
    return datetime.datetime.now()


def take(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry-excersise.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("successful written")

        elif c==2:
            value=input("type here\n")
            with open("harry-food.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("successful written")
    elif k==2:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("rohan-excersise.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("successful written")

        elif c==2:
            value=input("type here\n")
            with open("rohan-food.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("successful written")
    elif k==3:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("hamad-excersise.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("successful written")

        elif c==2:
            value=input("type here\n")
            with open("hamad-food.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("successful written")

    else:
        print("Enter valid input 1,2,3")

def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            
            with open("harry-excersise.txt") as op:
                for i in op:
                    print(i,end="")

        elif c==2:
            
            with open("harry-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
         
            with open("rohan-excersise.txt") as op:
                for i in op:
                    print(i,end="")

        elif c==2:
       
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==3:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            
            with open("hamad-excersise.txt") as op:
                for i in op:
                    print(i,end="")

        elif c==2:
            
            with open("hamad-food.txt") as op:
                for i in op:
                    print(i,end="")

    else:
        print("Enter valid input 1,2,3")

        

print("health management system")
a=int(input("Press 1 for log the value and 2 for rohan 3 for hamad"))

if a==1:
    b=int(input("Press 1 for harray 2 for rohan 3 for hamad"))
    take(b)
else:
    b=int(input("press 1 for harry 2 for "))


