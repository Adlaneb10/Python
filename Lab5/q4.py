# Prompt the user for three numbers and 
# print which is the largest of the three

num1_str = input("Enter your first number: ")
num2_str = input("Enter your second number: ")
num3_str = input("Enter your third number: ")

num1_int = int(num1_str)
num2_int = int(num2_str)
num3_int = int(num3_str)

max = num1_int

if max < num2_int:
    max = num2_int

if max < num3_int:
    max = num3_int


print("Largest number is ", max)
