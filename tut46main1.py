def myfun1(str):
    return f"this is string 1{str}"

def add(no1,no2):
    return no1+no2+4

print("and the main is ",__name__)

if __name__ == "__main__":
    print(myfun1("Hey"))
    o=add(3,4)
    print(o)