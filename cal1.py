def operation(op,n1,n2):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2
    elif op == "*":
        return n1-n2
    elif op == "/":
        return n1-n2
    elif op == "%":
        return n1-n2
    elif op == "**":
        return n1**n2
    else:
        print("Wrong Choice")
        


while(1):
    
    print("__________  Calculator by blu ______")
    operator = input("Enter Your Choice (+,-,*,/,%,**) :")
    No1=int(input("Enter no1 :"))
    No2=int(input("Enter no2 :"))

    ans=operation(operator,No1,No2)
    print("Your Answer  :",ans)
    que =input("Do you want to continue:  (y/n)")
    if que=="n":
        break
        

    







