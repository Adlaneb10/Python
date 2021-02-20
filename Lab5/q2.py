# Prompt the user to enter two integer numbers, 
# and output if the first is
#larger, smaller or equal to the second one. Use if-elif-else
#Author: Adlane Boulmelh
# Date: 29/09/2020

num1_str = input("Enter your first number: ")
num2_str = input("Enter your second number: ")

num1_int = int(num1_str)
num2_int = int(num2_str)

if num1_int > num2_int:
        print("First number is larger")
elif num1_int < num2_int:
    print("First number is smaller")
else:
    print("First number is equal to second number")

