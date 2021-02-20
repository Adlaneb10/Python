# Pyhton program to swap two random letters in a string
import random
string = input("Enter a string: ")

i = random.randint(0,len(string)-1)

j = random.randint(0,len(string)-1)

while i >= j:
    i = random.randint(0, len(string) - 1)
    j = random.randint(0, len(string) - 1)

new_s = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
print("result is: ", new_s)
print("chars swapped: ", string[i], string[j])