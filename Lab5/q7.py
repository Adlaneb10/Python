#How many three digit numbers are divisible by 17

count = 0
print("Numbers divisible by 17 are\n")
for i in range(100,1001+1):
    if i % 17 == 0:
        count = count + 1
        print(i)

print("\nThere are ",count,"divisible numbers ")
