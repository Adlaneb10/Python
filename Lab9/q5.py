def ent(int1):
    ans = 0
    fact = 1
    while(int1>1):
        fact *=  int1  
        int1 -= 1
        
        
    
    print("factorial is", fact)
    return int1

entry = int(input("Enter a number: "))
ent(entry)

