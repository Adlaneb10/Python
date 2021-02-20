string1 = "Hello"

#print(string1[::-1])
i = 0
for i in range(4,-1,-1):
    string1 = string1[i] + string1[i-1] + string1[i-2] + string1[i-3] + string1[i-4]
    break
print(string1)