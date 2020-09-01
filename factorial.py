
#n!= n*(n-1)*(n-2)*(n-3).....!
#n!= n*(n-1)!

def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

 
number= int(input("Enter our number:"))
print("Factorial using Iterative Method",factorial(number))


def recursive(n):
  
    if n==1:
        return 1
    else:
        return n*recursive(n-1)

 
number= int(input("Enter our number:"))
print("Factorial using Recursive Method",recursive(number))


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  fibonacci(n-1)+fibonacci(n-2) 

number=int(input("Enter number"))
print(fibonacci(number))