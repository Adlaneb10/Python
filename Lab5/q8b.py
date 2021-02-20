#b
num = int(input("Enter a number: "))

for i in range(1,num+1):
    sum = 0
    for j in range(1,i+1):
        sum += j
        if j<i:
            print(j," + ",end= "")
        else:
            print(j,"=", end =" ")
    
    print(sum)

#c)
for i in range(1,num+1):
    sum = 0
    count = 0
    result =""
    for j in range(1,i+1):
        sum += j
        count += 1
        if j<i:
            result += str(j) + " + "
        else:
            result += str(j) + " = "
    if sum % count == 0:
        print(result,sum)
