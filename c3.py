print("_____tut24")
print("Try _ catch\n\n")
n1=input("no1")
n2=input("no2")
try:
    print(int(n1)+int(n2))
except Exception as e:
    print(e)

print("all time execute")

print("______tut26 file io")

#r- read mode
#w- write mode
#x - exclusive mode create file if not exists
#a - add more content to file

#t - text mode
#b - binary mode
#+ - read and write mode


f=open("myfile.txt","rt")
# content = f.read()
# print(content)
# content = f.read(3)
# print(content)

# print(f.readline())
print(f.readlines())

# for line in f:
#     print(line)
# f.close()

f=open("myfile.txt","a")
f.write("Commit")
f.close()

f=open("myfile.txt","r+")
f.write("Commit")
f.close()

