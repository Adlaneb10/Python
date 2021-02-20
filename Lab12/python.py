myfile = open("filetest.txt")
lines = myfile.readlines()
for line in lines:
    print(line)

myfile.close()