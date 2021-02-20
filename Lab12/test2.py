myfile = open("filetest.txt")
txt = myfile.readlines()
for line in txt:
    print(line)
myfile.close()