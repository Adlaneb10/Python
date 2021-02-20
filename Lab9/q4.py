def ent(int1):
    ans = 0
    for i in range(0,int1+1):
        ans += i
        print(int1, i)
    print("The sum is ",ans)
    return int1

entry = int(input("Enter a number: "))
ent(entry)

