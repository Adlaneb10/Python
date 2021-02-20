
f1 = open("filetest.txt","r")


print("Name of the file:", f1.name)

lines = f1.readlines()
for line in lines:
    print(line)


f1.close()
