string = "Monty Python"

#print first character 3a)
print(string[0], "3a")

print("\n")

#print last char (b)
print(string[-1], "b")

print("\n")

for index in range(len(string)):
    print(string[-1], "(c)")
    break

for i in range(0,5):
    print(string[i])