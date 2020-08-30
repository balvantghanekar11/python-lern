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
