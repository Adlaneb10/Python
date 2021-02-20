d = {'a':3,'x':7,'r':5}

# Code that returns value at key 'x'
print(d["x"])
print(d)

#Code which returns the key given value 7

for key,value in d.items():
    if value == 7:
        print(key)

list2 = []
list = [1,"H",2,"y",3,"o",4,"p",5,"l",6]
for el in list:
    #print(el,end=" ")
    if type(el) == int:
        list2.append(el)
    #else:
     #   pass
print(list2)
#total = sum(list[1:-1:2])
#print(total)
