#python program to encrypt a string

string = "abc"

num1 = ord(string[0])
num2 = ord(string[1])
num3 = ord(string[2])

num1 += 1
num2 += 1
num3 += 1

str_new1 = chr(num1)
str_new2 = chr(num2)
str_new3 = chr(num3)

encrypted_str = str_new1 + str_new2 + str_new3

print(encrypted_str)