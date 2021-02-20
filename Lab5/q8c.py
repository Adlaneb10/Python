my_int = int(input("enter a number: "))

for i in range(1,my_int+1):
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