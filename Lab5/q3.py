# Write a small calculator simulator – 
# ask the user to enter two numbers 
# and an operation (+, -, *, /), and either add, 
# subtract, multiply or divide the numbers, and print the result.
#Author: Adlane Boulmelh
# Date: 29/09/2020


num1_str = input("Enter your first number: ")
num2_str = input("Enter your second number: ")

num1_int = int(num1_str)
num2_int = int(num2_str)

oper_str = input("What operation would you like to do? : ")

if oper_str == '+':
    sum = num1_int + num2_int
    print("Result is ", sum)

elif oper_str == '-':
    minus = num1_int - num2_int
    print("Result is ",minus)

elif oper_str == '*':
    mult = num1_int * num2_int
    print("Result is ", mult)

elif oper_str == '/':
    div = num1_int / num2_int
    print("Result is ", div)

