def ent(int1):
    for i in range(0,int1+1):
        print(i)
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")
    return int1

entry = int(input("Enter a number: "))
ent(entry)

